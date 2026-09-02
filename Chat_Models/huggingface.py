# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
load_dotenv()
# pyrefly: ignore [missing-import]
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

response = model.invoke('tell me in 10 lines about imran khan in pakistan')
print(response.content)