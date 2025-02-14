"""Example script for using the mock search agent."""
from langchain.agents.mock_search_agent import MockSearchAgent

def main():
    """Run the QA interface."""
    agent = MockSearchAgent()
    print("Mock Search QA System")
    print("Type 'exit' to quit\n")
    
    while True:
        question = input("\nEnter your question: ")
        if question.lower() == 'exit':
            break
            
        try:
            response = agent.run(question)
            print("\nResponse:")
            print(response)
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()
