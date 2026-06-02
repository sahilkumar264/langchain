from langchain_google_genai import ChatGoogle
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatGoogle(model="gemini-2.0-pro", temperature = 0.7 , max_completion_tokens=2048)
result = chat_model.invoke("What is the capital of india?")
print(result.content) #result.content only answer of the question, without any additional information
