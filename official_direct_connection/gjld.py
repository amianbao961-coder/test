from openai import OpenAI

client = OpenAI(
    api_key="sk-grhnhvjraxtqnpbvmyeszfominmfzhliuexfrxysgzcwzhjw",
    base_url="https://api.siliconflow.cn/v1"
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V4-Flash",
    messages=[
        #{"role": "system", "content": "你是一个万事通ai，擅长帮人们解决各种问题"},
        {"role": "user", "content": "一句话介绍一下自己"}
    ]
)
print(response.choices[0].message.content)
