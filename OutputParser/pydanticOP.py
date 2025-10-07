from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()
llm = HuggingFaceEndpoint(
    model="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)
lm = ChatHuggingFace(llm=llm)
class Person(BaseModel):
    name : str = Field(description='name of the person')
    age : int = Field(gt=18,description='Age of the person')
    city : str = Field(description='City from which that person belongs')

parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template='Give me name , age, city of a {place} person\n {format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)
# prompt = template.invoke({'place':'indian'})
# result = lm.invoke(prompt)
# final = parser.parse(result.content)
# print(final)
chain = template | lm |parser
result = chain.invoke({'place':'indian'})
print(result)