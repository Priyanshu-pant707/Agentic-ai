from dotenv import load_dotenv


load_dotenv()


from langchain_mistralai import ChatMistralAI


model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

print("Chatbot is ready! Start chatting with the bot (type 'exit' to quit).")

while True:
    prompt=input("YOU: ")
    if(prompt=="exit"):
        print("Exiting the chat. Goodbye!")
        break
    response=model.invoke(prompt)
    print("BOT: ",response.content)
