from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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
parser = StrOutputParser()
chain = template1 | lm |parser| summarizer | lm | parser
result = chain.invoke({'topic':'Lionel Messi '})
print(result)


