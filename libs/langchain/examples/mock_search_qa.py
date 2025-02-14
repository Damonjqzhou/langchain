"""Example script for using the mock search agent."""
import sys
from langchain.agents.mock_search_agent import MockSearchAgent

def main():
    """Run the QA interface."""
    # Basic script setup - no explicit encoding handling needed
    # Python 3 handles UTF-8 by default when PYTHONIOENCODING is set
    pass
    
    agent = MockSearchAgent()
    print("Mock Search QA System (支持中文)")
    print("输入 'exit' 退出\n")
    
    while True:
        question = input("\n请输入您的问题: ")
        if question.lower() == 'exit':
            break
            
        try:
            response = agent.run(question)
            print("\n回答:")
            print(response)
        except Exception as e:
            print(f"\n错误: {str(e)}")

if __name__ == "__main__":
    main()
