from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = GoogleGenerativeAI(model="gemini-2.5-flash")
result = model.invoke("Write a poem in 10 words on cricket in winters in india")
print(result)
print(getattr(result, "content", getattr(result, "text", str(result))))
