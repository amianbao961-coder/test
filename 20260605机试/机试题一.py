from langchain_deepseek import ChatDeepSeek
import os
import dotenv
import asyncio
dotenv.load_dotenv()

llm=ChatDeepSeek(
    model="deepseek-ai/DeepSeek-V4-Flash",
    base_url=os.getenv("GJ_BASE_URL"),
    api_key=os.getenv("GJ_API_KEY"),
    max_tokens=2048
)
async def main():
    response=await llm.ainvoke("请写一首歌，不限主题")
    print(response.content)
    print(f"Token消耗: {response.usage_metadata['total_tokens']}")

asyncio.run(main())
