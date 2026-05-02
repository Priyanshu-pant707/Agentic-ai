from dotenv import load_dotenv

load_dotenv()



from langchain.chat_models import init_chat_model

model =init_chat_model(model="mistral-small-2506", temperature=0.9)

responce = model.invoke("What is the capital of France?")
print(responce.content)

