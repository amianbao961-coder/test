import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()
# 一个函数搞定所有提供商，通过model_provider 参数区分
llm_openai = init_chat_model(
	model="GLM-5.1",
	model_provider="openai",# 模型
	api_key=os.getenv("ZP_API_KEY"),
	base_url=os.getenv("ZP_BASE_URL")
)
llm_claude = init_chat_model(
	model="deepseek-ai/DeepSeek-V4-Flash",
	model_provider="openai",
	api_key=os.getenv ("GL_API_KEY"),
	base_url=os.getenv("GL_BASE_URL")
)
llm_gemini = init_chat_model(
	model="Pro/moonshotai/Kimi-K2.6", # 文本模型
	model_provider="openai",
	api_key=os.getenv("GL_API_KEY"),
	base_url=os.getenv("GL_BASE_URL")
)
#调用方式完全一致
for name, llm in [("GLM", llm_openai), ("DeepSeek", llm_claude), ("Kimi", llm_gemini) ]:
	response=llm.invoke("用一句话介绍你自己")
	print(f"{name}: {response.content}")