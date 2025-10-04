from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a halpful {domain} expert"),
        ("human", "Explain in simple terms what is this {topic}"),
    ]
)
prompt = chat_template.invoke({"domain": "cricket", "topic": "virat Kohli"})
print(prompt)
