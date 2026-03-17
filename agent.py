from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.chat_models import ChatOllama
from langchain import hub
from tools import tools

# Load prompt for react agent
prompt = hub.pull("hwchase17/react")

# Local LLM
llm = ChatOllama(model="llama3")

# Create agent
agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

while True:
    question = input("\nAsk something: ")

    if question.lower() == "exit":
        break

    response = agent_executor.invoke({"input": question})

    print("\nAnswer:", response["output"])