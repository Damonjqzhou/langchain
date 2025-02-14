"""Agent that uses mock search tool for development and testing."""
from typing import List, Optional
from langchain.tools.mock_search import MockSearchTool
from langchain_core.prompts import PromptTemplate

MOCK_AGENT_TEMPLATE = """You are a helpful AI assistant that uses search to answer questions.
When you receive a question, you will get search results to help answer it.
Use the search results to provide an informative answer.

Question: {question}
Search Results: {search_results}

Answer: Based on the search results, I can tell you that this topic has shown significant developments. Experts consider it an important area of research, and recent findings indicate positive trends."""

class MockSearchAgent:
    """Agent that uses mock search for answering questions."""
    
    def __init__(self):
        """Initialize the mock search agent."""
        self.search_tool = MockSearchTool()
        self.prompt = PromptTemplate(
            template=MOCK_AGENT_TEMPLATE,
            input_variables=["question", "search_results"]
        )
    
    def run(self, question: str) -> str:
        """Run the agent on a given question."""
        search_results = self.search_tool.run(question)
        return self.prompt.format(
            question=question,
            search_results=search_results
        )
