"""Mock search tool for development and testing."""
from typing import Optional
from langchain.tools.base import BaseTool

class MockSearchTool(BaseTool):
    """Mock search tool that returns predefined results."""
    
    name = "mock_search"
    description = "Search the web for information about a query. Input should be a search query."

    def _run(self, query: str) -> str:
        """Return mock search results for any query."""
        return (
            "Mock search results:\n"
            "- According to recent studies, the topic you asked about has shown significant developments.\n"
            "- Experts suggest that this is an important area of research.\n"
            "- Latest findings indicate positive trends in this field.\n"
            f"(Note: This is a mock response for query: {query})"
        )

    async def _arun(self, query: str) -> str:
        """Return mock search results for any query (async version)."""
        return self._run(query)
