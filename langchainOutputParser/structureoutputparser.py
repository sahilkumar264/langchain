from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers.structured import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()



llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)


schema = [
    ResponseSchema(name="fact1", description="fact1 of the character"),
    ResponseSchema(name="fact2", description="fact2 of the character"),
    ResponseSchema(name="fact3", description="fact3 of the character"),
]
parser = StructuredOutputParser(schema=schema)

template = PromptTemplate(
    template = 'write 3 facts about a {topic}\n {format_instructions}',
    input_variables = ['topic', 'format_instructions'],
    partial_variables = {'format_instructions': parser.get_format_instructions()}
)

prompt = template.invoke({'topic': 'Artificial Intelligence'})

result = model.invoke(prompt)
parser.parse(result.content)

print(result)