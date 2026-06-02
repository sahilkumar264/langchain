from langchain_huggingface import HuggingFaceEmbeddings 

llm = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

text = "What is the capital of India?"
vector = llm.embed_query(text)

print(str(vector))