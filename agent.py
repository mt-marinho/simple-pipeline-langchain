
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

load_dotenv()

model = init_chat_model("google_genai:gemini-3.5-flash")

my_agent = create_agent(
    model=model, 
    system_prompt="se voce não souber a resposta busque no google usando o tavily search",
    tools=[TavilySearch()]
)

pergunta = "busque a temperatura de campo grande ms atualmente usando o tevily"
resposta = my_agent.invoke({"messages": [{"role": "user", "content": pergunta}]})
print(resposta["messages"][-1].text)