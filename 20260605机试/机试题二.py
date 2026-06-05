from langchain_deepseek import ChatDeepSeek
import os
import dotenv
dotenv.load_dotenv()

llm=ChatDeepSeek(
    model="deepseek-ai/DeepSeek-V4-Flash",
    base_url=os.getenv("GJ_BASE_URL"),
    api_key=os.getenv("GJ_API_KEY"),
)
questions=[
    "你是谁？",
    "你能帮助我吗？",
    "你是ai吗？"
]
responses = llm.batch(questions)
total_tokens = 0
for q, r in zip(questions, responses):
    print(f"Q: {q}")
    print(f"A: {r.content}\n")
    total_tokens += r.usage_metadata['total_tokens']
print(f"Token消耗: {total_tokens}")