from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = GoogleGenerativeAI(model="gemini-2.5-flash")
messsages = [
    SystemMessage(content = 'You are a helpful ai assistant'),
    HumanMessage(content='Tell me about yourself')
]
result=model.invoke(messsages)
messsages.append(AIMessage(content=result))
print(messsages)