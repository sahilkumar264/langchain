from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
# as we did not give openAi key so it will not work
embedding = OpenAIEmbeddings(model="text-embedding-3-large" , dimension = 32)
document = [
    "delhi is capital of india",
    "kolkata is capital of west begal"
]

result = embedding.embed_documents(document)

print(str(result)); #result is a list of list, where each inner list is the embedding of the corresponding document in the input list.