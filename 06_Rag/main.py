from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Load document
data = TextLoader("doc_loader/notes.txt")
doc = data.load()

# Correct prompt template
template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI that summarizes the text"),
    ("human", "{data}")
])

# Model
model = ChatMistralAI(model="mistral-small-latest")

# Correct method
prompt = template.format_messages(data=doc[0].page_content)

# Invoke model
result = model.invoke(prompt)

print(result.content)