
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

load_dotenv()

model = init_chat_model("google_genai:gemini-3.5-flash")

my_agent = create_agent(
    model=model, 
    system_prompt="responda oque voce sabe, se não souber diga que não sabe, não tente inventar respostas",
    tools=[TavilySearch()],
)

config = {"configurable": {"thread_id": "nome"}}


def run_cli():
    print("agente em funcionamento")
    while True:
        user_input = input("Digite sua pergunta: ")
        response = my_agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config,
        )
        print(f"Agente: {response['messages'][-1].content}")


if __name__ == "__main__":
    run_cli()
