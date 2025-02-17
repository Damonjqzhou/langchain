"""Unit tests for code translation tools."""
from langchain.tools.code_translation.base import CodeTranslationTool

def test_code_translation_tool() -> None:
    """Test basic code translation functionality."""
    tool = CodeTranslationTool()
    result = tool.run({
        "source_code": "NSString *str = @\"Hello\";",
        "source_language": "objective-c",
        "target_language": "cpp",
        "preserve_comments": True
    })
    assert "std::string" in result

def test_code_translation_tool_validation() -> None:
    """Test input validation."""
    tool = CodeTranslationTool()
    try:
        tool.run({
            "source_code": "var x = 5;",
            "source_language": "javascript",  # Unsupported language
            "target_language": "cpp",
            "preserve_comments": True
        })
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
