from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatAnthropic(model="claude-3-opus-20241209", temperature = 0.7 , max_completion_tokens=2048)

result = chat_model.invoke("What is the capital of india?")

print(result.content) #result.content only answer of the question, without any additional information