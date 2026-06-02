from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4", temperature = 0.7 , max_completion_tokens=2048)
#we also have temprature parameter which is used to control the randomness of the output, higher the temperature more random the output will be, you can set it between 0 and 1, default is 0.7
#max_completion_toke is used to control the maximum number of tokens in the output, you can set it according to your requirement, default is 2048
result = chat_model.invoke("What is the capital of india?")

print(result.conent) #result.content only answer of the question, without any additional information
print(result) # result will give you the complete response, including additional information if any

