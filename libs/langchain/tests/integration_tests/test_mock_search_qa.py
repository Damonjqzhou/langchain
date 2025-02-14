"""Integration tests for mock search QA system."""
import pytest
from langchain.agents.mock_search_agent import MockSearchAgent

def test_mock_search_qa_basic():
    """Test basic QA functionality."""
    agent = MockSearchAgent()
    question = "What is machine learning?"
    response = agent.run(question)
    
    # Verify response structure
    assert "Question:" in response
    assert question in response
    assert "Search Results:" in response
    assert "Mock search results:" in response
    assert "Answer:" in response

def test_mock_search_qa_fixed_content():
    """Test that search results are fixed mock content."""
    agent = MockSearchAgent()
    questions = [
        "What is AI?",
        "Tell me about robots",
        "Explain quantum computing"
    ]
    
    responses = [agent.run(q) for q in questions]
    
    # Verify all responses contain the same mock search pattern
    for response in responses:
        assert "significant developments" in response
        assert "important area of research" in response
        assert "positive trends" in response
