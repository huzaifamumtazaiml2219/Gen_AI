from dotenv import load_dotenv
load_dotenv()
# pyrefly: ignore [missing-import]
from langchain_openai import OpenAIEmbeddings
# embeddings = OpenAIEmbeddings(
#     model = 'text-embedding-3-large',
#     dimensions= 64
# )
# vector = embeddings.embed_query("Hello World")
embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimensions= 64
)
text = [
    'Hello how are you?',
    'How are you doing today?',
    'What is the weather like?'
]
vector = embeddings.embed_documents(text)
print(vector)