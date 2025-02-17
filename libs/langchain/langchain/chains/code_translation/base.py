"""Chain for translating code between programming languages."""
from typing import Any, Dict, List, Optional

from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseTool

from langchain.agents import AgentExecutor
from langchain.agents.code_translation.base import create_code_translation_agent
from langchain.chains.base import Chain
from langchain.tools.code_translation.base import CodeTranslationTool

class CodeTranslationChain(Chain):
    """Chain for translating code between programming languages."""

    agent: AgentExecutor
    tools: List[BaseTool]

    @property
    def input_keys(self) -> List[str]:
        """Return the input keys.

        Returns:
            List of input keys.
        """
        return ["input"]

    @property
    def output_keys(self) -> List[str]:
        """Return the output keys.

        Returns:
            List of output keys.
        """
        return ["output"]

    def _call(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        """Run the chain.

        Args:
            inputs: Chain inputs.

        Returns:
            Chain outputs.
        """
        return {"output": self.agent.run(inputs)}

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        tools: Optional[List[BaseTool]] = None,
        **kwargs: Any,
    ) -> "CodeTranslationChain":
        """Create a chain from a language model.

        Args:
            llm: The language model to use.
            tools: Optional list of tools. If not provided, will use CodeTranslationTool.
            **kwargs: Additional arguments to pass to the chain.

        Returns:
            A code translation chain.
        """
        tools = tools or [CodeTranslationTool()]
        agent = create_code_translation_agent(llm, tools)
        executor = AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=tools,
            **kwargs,
        )
        return cls(agent=executor, tools=tools)
