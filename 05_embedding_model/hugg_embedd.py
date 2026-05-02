from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings

# Initialize embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Test text
text = "What is the capital of France?"

# Get embedding vector
vector = embeddings.embed_query(text)

print("Embedding vector length:", len(vector))
print(vector[:10])   # first 10 values