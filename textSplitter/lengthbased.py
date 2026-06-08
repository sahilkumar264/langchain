from langchain.text_splitter import CharacterTextSplitter , RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


#let suppose we have a pdf named input.pdf

loader = PyPDFLoader('input.pdf')
docs = loader.load()
# splitter = CharacterTextSplitter(
#     chunck_size = 100,
#     chunk_overlap = 0, #overlap meanaing how many text is will overlap in between 2 continues chunk 
#     seprator = ''
# )

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 300,
#     chunk_overlap = 0
# )

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 300,
    chunk_over = 0 
)

result = splitter.split_documents(docs)
print(result)