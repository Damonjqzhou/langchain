"""Agent for translating code between programming languages."""
from typing import Optional, Sequence

from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import BaseTool

from langchain.agents.xml.base import XMLAgent
from langchain.tools.code_translation.base import CodeTranslationTool


def create_code_translation_agent(
    llm: BaseLanguageModel,
    tools: Optional[Sequence[BaseTool]] = None,
) -> XMLAgent:
    """Create an agent specialized for code translation tasks.
    
    Args:
        llm: The language model to use
        tools: Optional sequence of tools. If not provided, will use CodeTranslationTool
        
    Returns:
        An XMLAgent configured for code translation
    """
    tools = tools or [CodeTranslationTool()]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a code translation expert specializing in translating 
        Objective-C code to C++ QTT. Translate code while preserving:
        1. Program logic and functionality
        2. Code structure and organization
        3. Comments and documentation (if preserve_comments is True)
        4. Variable and function naming conventions appropriate for target language
        
        You have access to the following tools:
        
        {tools}
        
        Use XML tags to specify your actions. For example:
        <tool>code_translator</tool>
        <tool_input>
        {{"source_code": "NSString *str = @\\"Hello\\";", 
         "source_language": "objective-c",
         "target_language": "cpp",
         "preserve_comments": true}}
        </tool_input>
        
        Always validate your translations to ensure they maintain functionality.
        """),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    return XMLAgent.from_llm_and_tools(
        llm=llm,
        tools=tools,
        prompt=prompt
    )
