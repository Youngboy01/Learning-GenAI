from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema,StructuredOutputParser
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    model="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)
lm = ChatHuggingFace(llm=llm)
schema = [
    ResponseSchema(name='fact1', description='Fact1 about the topic'),
    ResponseSchema(name='fact2', description='Fact2 about the topic'),
    ResponseSchema(name='fact3', description='Fact3 about the topic'),
    ResponseSchema(name='fact4', description='Fact4 about the topic')
]
parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template='Give me 4 facts about the {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)
# prompt = template.invoke({'topic':'BlackHole'})
# result = lm.invoke(prompt)
# final = parser.parse(result.content)
# print(final)
chain = template | lm | parser
result = chain.invoke({'topic':'Messi'})
print(result)