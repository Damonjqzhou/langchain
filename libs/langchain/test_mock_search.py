"""Test script for mock search tool."""
from langchain.tools.mock_search import MockSearchTool

def main():
    tool = MockSearchTool()
    result = tool.run("test query")
    print(result)

if __name__ == "__main__":
    main()
