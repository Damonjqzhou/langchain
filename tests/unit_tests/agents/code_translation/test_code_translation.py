"""Unit tests for code translation agents."""
from unittest.mock import Mock

from langchain.agents.code_translation.base import create_code_translation_agent
from langchain.tools.code_translation.base import CodeTranslationTool

def test_code_translation_agent() -> None:
    """Test basic agent functionality."""
    # Mock LLM that returns a valid XML response
    mock_llm = Mock()
    mock_llm.predict_messages.return_value.content = """
    <tool>code_translator</tool>
    <tool_input>
    {"source_code": "NSString *str = @\\"Hello\\";", 
     "source_language": "objective-c",
     "target_language": "cpp",
     "preserve_comments": true}
    </tool_input>
    <final_answer>Translation complete: std::string str = "Hello";</final_answer>
    """
    
    agent = create_code_translation_agent(
        llm=mock_llm,
        tools=[CodeTranslationTool()]
    )
    
    result = agent.plan(
        intermediate_steps=[],
        input="Translate this Objective-C code: NSString *str = @\"Hello\";"
    )
    assert "std::string" in str(result)
