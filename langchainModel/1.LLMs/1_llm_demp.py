from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(model="gpt-3.5-turbo-instruct") 
# since we don't have api key, we will not be able to run the code, but you can run it in your local environment after setting up the api key in .env file

result = llm.invoke("What is the capital of India?")
print(result)
