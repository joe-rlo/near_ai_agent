def main():
    """Example script to run the agent"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Run the NEAR AI agent")
    parser.add_argument("--local", action="store_true", help="Run in local mode")
    parser.add_argument("--execution_folder", default="/tmp/agent_run", 
                       help="Folder for agent execution")
    
    args = parser.parse_args()
    
    # Create agent with no environment for local testing
    agent = NearAIAgent()
    agent.run()

if __name__ == "__main__":
    main()