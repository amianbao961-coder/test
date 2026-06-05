from langchain_deepseek import ChatDeepSeek
import os
import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
dotenv.load_dotenv()

llm = ChatDeepSeek(
    model="deepseek-ai/DeepSeek-V4-Flash",
    base_url=os.getenv("GJ_BASE_URL"),
    api_key=os.getenv("GJ_API_KEY"),
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是AI万事通助手"),
    ("placeholder", "{history}"),
    ("human", "{input}"),
])

messages = prompt.invoke({
    "history": [
        HumanMessage(content="什么是Python？"),
        AIMessage(content="Python是一种通用编程语言。"),
    ],
    "input": "它有什么特点？"
})
response = llm.invoke(messages)
print(response.content)
print(f"Token消耗: {response.usage_metadata['total_tokens']}")