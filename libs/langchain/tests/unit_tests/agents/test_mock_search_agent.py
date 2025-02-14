"""Tests for mock search agent."""
from langchain.agents.mock_search_agent import MockSearchAgent

def test_mock_search_agent():
    """Test that mock search agent returns expected format."""
    agent = MockSearchAgent()
    result = agent.run("What is artificial intelligence?")
    assert isinstance(result, str)
    assert "Question:" in result
    assert "Search Results:" in result
    assert "Answer:" in result
