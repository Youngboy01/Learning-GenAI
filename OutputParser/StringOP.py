from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = HuggingFaceEndpoint(
    model="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
summarizer = PromptTemplate(
    template = 'Write a 5 line summary on the following text./n {text}',
    input_variables=['text']
)
lm = ChatHuggingFace(llm=llm)
prompt1 = template1.invoke({'topic':'Lionel Messi'})
result=lm.invoke(prompt1)
prompt2 = summarizer.invoke({'text':result.content})
ans = lm.invoke(prompt2)
print(ans.content)
