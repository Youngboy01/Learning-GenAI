from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
docs=[
    "Delhi is india",
    "kolkata is notindeoa",
    "pakistana is kachra"
]
result=embeddings.embed_documents(docs)
print(str(result))
