from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs  = dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)
# result = model.invoke("What is the capital of india?");
# print(result.content)

chat_history = []

while True:
    user_input = input("Enter prompt: ")
    chat_history.append(user_input)
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print(result.content)