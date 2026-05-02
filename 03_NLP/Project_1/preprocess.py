import re # Regular expressions - for extracting and removing  the numbers,punctuations ,emojis and the html tags 
# two powerful libraries for NLP tasks
import nltk # tokenization and stopword removal
import spacy # lemmatization


# tools from nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download once (safe even if already downloaded)
nltk.download('punkt')  # rule required for the sentence and word tokenization
nltk.download('punkt_tab') # tokenization table
nltk.download('stopwords') # English stopword lists

# Load spaCy model- english language small model
# model contains - grammar rules,lemmatization logic , pos tagging, dependency parsing 
nlp = spacy.load("en_core_web_sm")


# ---------------- CLEAN TEXT ----------------
def clean_text(text: str) -> str:
    """
    Lowercase, remove punctuation, numbers, emojis, extra spaces
    """
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)              # remove HTML
    text = re.sub(r'[^a-zA-Z\s]', '', text)        # remove numbers & punctuation
    text = re.sub(r'\s+', ' ', text).strip()       # remove extra spaces
    return text


# ---------------- TOKENIZATION ----------------
def tokenize_text(text: str) -> list:
    """
    Break sentence into words
    """
    return word_tokenize(text)


# ---------------- STOPWORD REMOVAL ----------------
def remove_stopwords(tokens: list) -> list:
    """
    Remove common useless words
    """
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]


# ---------------- LEMMATIZATION ----------------
def lemmatize_text(text: str) -> list:
    """
    Convert words into their dictionary form
    """
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop]


# ---------------- FULL PIPELINE ----------------
def preprocess_pipeline(text: str) -> dict:
    """
    Complete NLP preprocessing pipeline
    """
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)
    tokens_no_stopwords = remove_stopwords(tokens)
    lemmatized_tokens = lemmatize_text(cleaned_text)

    return {
        "cleaned_text": cleaned_text,
        "tokens": tokens,
        "tokens_no_stopwords": tokens_no_stopwords,
        "lemmatized_tokens": lemmatized_tokens
    }


# ---------------- TESTING ----------------
if __name__ == "__main__":
    sample_text = "I am learning NLP in 2025! It's awesome 😊"
    output = preprocess_pipeline(sample_text)

    for key, value in output.items():
        print(f"{key}: {value}")
