from dotenv import load_dotenv
load_dotenv()
# pyrefly: ignore [missing-import]
# from langchain.chat_models import init_chat_model
# from langchain_groq import ChatGroq
# from langchain_mistralai import ChatMistralAI
# pyrefly: ignore [missing-import]
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
# model = ChatGroq(model='openai/gpt-oss-120b')
# model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')
# model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')
# model = init_chat_model('gpt-4.1')
# model_gpt = ChatOpenAI(model='gpt-4.1')
# print (model)
# response = model.invoke('tell me about imran khan in pakistan in short')
# print(response.content)
model = ChatOpenAI(model="gpt-4.1", temperature=0)
print("chosse your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode ")
print("press 3 for sad mode")
choice = int(input("tell your response :- "))
if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."

message = [
    SystemMessage(content=mode)
]
print ('----------------Welcome!, press 0 to exit----------')
while True:
    prompt = input('You: ')
    if prompt == "0":
        break
    message.append(HumanMessage(content=prompt))
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print('Bot:', response.content)
