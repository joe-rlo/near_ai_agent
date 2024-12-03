from near_ai_agent.agent import NearAIAgent

agent = NearAIAgent()

# Set and retrieve context
agent.environment.set_context("user_id", "12345")
context = agent.environment.get_context()
print(f"Initial Context: {context}")

# Execute tasks
agent.handle_task("fetch_user_info", "12345")
agent.handle_task("provide_weather", "Paris")

# Retrieve updated context
updated_context = agent.environment.get_context()
print(f"Updated Context: {updated_context}")