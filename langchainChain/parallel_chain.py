from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)
parser = StrOutputParser()

template1 = PromptTemplate(
    template = "write notes of this text {text}",
    input_variables=["text"]
)

template2 = PromptTemplate(
    template = "Generate 5 question on following text {text}",
    input_variables=["text"]
)

template3 = PromptTemplate(
    template = "merge notes and question {notes} and {question}",
    input_variables=["notes" , "question"]
)


parallel_chain = RunnableParallel({
    "notes": template1 | model | parser,
    "question": template2 | model | parser 
})


merge_chain = template3 | model | parser

chain = parallel_chain | merge_chain

text = "Lumos Learning offers a free online Question and Answer Generator that allows you to paste any text—including essays, stories, or passages—to automatically generate questions and answers for note-taking and study.  You can also generate Q&As directly from YouTube video transcripts by copying the text from the video's transcript section. Alternatively, Random Passages provides a curated collection of memorable literary excerpts and writing samples.  You can select any random passage from this site to use as a basis for analyzing themes, vocabulary, or narrative structure. For broader discussion, Random Topic Generator tools (such as those on The Story Shack or CodeBeautify) provide specific subjects or conversation starters across categories like science, history, and philosophy, which you can then research and question independently."

result = chain.invoke({"text": text})

print(result)

chain.get_graph().print_ascii()