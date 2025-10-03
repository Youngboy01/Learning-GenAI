from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
import os
os.environ['HF_HOME']= 'D:/ huggingface_cache'
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens =512
    )
)
chat = ChatHuggingFace(llm=llm)
result = chat.invoke("who are you")
print(result)