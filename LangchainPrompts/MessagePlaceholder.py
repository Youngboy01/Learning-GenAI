from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
chat_template = ChatPromptTemplate([
    ("system", "You are a halpful customer support agent"),
    MessagesPlaceholder(variable_name='chatHistory.txt'),
    ("human", "{query}")
])
chat_history=[]
with open('chatHistory.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)
prompt = chat_template.invoke({'chat_history':chat_history,'query':'Where is my refund?'})
print(prompt)