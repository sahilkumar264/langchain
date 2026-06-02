from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

llm  = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2");

document = [
    "Virat kohli is a great cricketer",
    "Sachin tendulkar is a old great cricketer",
    "Rohit sharma is a good opener cricketer",
    "MS dhoni is a best wicket keeper and finisher cricketer"
]
query = "Who is the virat kholi?"

embed_document = llm.embed_documents(document)
embed_query = llm.embed_query(query)


cosine_sim = sorted(enumerate(cosine_similarity([embed_query], embed_document)[0]), key = lambda x : x[1] , reverse = True) 
for index, score in cosine_sim:
    print(f"Score: {score:.4f}")
    print(f"Document: {document[index]}")
    print("-" * 50)