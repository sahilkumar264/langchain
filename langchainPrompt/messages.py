from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
from langchain_core.messages import HumanMessage, AIMessage , SystemMessage

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs  = dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of India?")
]

model = ChatHuggingFace(llm=llm)
result = model.invoke(messages)

messages.append(AIMessage(result.content))
print(messages)