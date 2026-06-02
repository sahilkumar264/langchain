from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
# from dotenv import load_dotenv
# load_dotenv()


#it will download the model and store it in cache directory, so it will work without internet connection after first run
# as tinyllm is a small model, it will not take much time to download and run, you can also try with larger models like llama 3.1 or falcon 40b, but they will take more time to download and run
llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs  = dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of india?");
print(result.content)