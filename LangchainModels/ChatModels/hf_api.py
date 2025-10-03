from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    task="conversational",
    max_new_tokens=512
)

chat = ChatHuggingFace(llm=llm)

result = chat.invoke("what is the capital of india?")
print(result.content) 

