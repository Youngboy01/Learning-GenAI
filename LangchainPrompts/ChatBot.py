from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()
model = GoogleGenerativeAI(model="gemini-2.5-flash")
chat_history =[]
chat_history.append(SystemMessage(content = 'You are a helpful ai assistant'))
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print("Gemini: ",result)
print(chat_history)
