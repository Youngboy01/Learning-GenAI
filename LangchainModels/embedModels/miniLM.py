from langchain_huggingface import HuggingFaceEmbeddings
import os
os.environ['HF_HOME']= 'D:/huggingface_cache'
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')#gives 384 dim vector
text = "My name is Mitanshu"
vector = embedding.embed_query(text)
print(str(vector))