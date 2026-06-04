from langchain_deepseek import ChatDeepSeek
import os
# from langchain_core.messages import SystemMessage, HumanMessage
import dotenv
dotenv.load_dotenv()

llm=ChatDeepSeek(
    model="GLM-5.1",
    base_url=os.getenv("ZP_BASE_URL"),
    api_key=os.getenv("ZP_API_KEY")
)
#快捷
response=llm.invoke("一句话介绍你自己")
print(response.content)
#上下文
# response=llm.invoke([
#     SystemMessage(content="你是一个情感专家!"),
#     HumanMessage(content="我好难受!安慰下我")
# ])
