"""Tests for mock search tool."""
from langchain.tools.mock_search import MockSearchTool

def test_mock_search():
    """Test that mock search returns expected format."""
    tool = MockSearchTool()
    result = tool.run("test query")
    assert isinstance(result, str)
    assert "Mock search results:" in result
    assert "test query" in result
