from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
llm = HuggingFaceEndpoint(
    model="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)
lm = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()
template1 = PromptTemplate(
    template='Give me name , age, city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt = template1.format()
# result = lm.invoke(prompt)
# # print(result)
# ans = parser.parse(result.content)
# print(ans)
# print(type(ans))
chain = template1 | lm | parser
res = chain.invoke({})
print(res)