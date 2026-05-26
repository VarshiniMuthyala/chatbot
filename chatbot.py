import json
import random
import nltk

from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download nltk data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

patterns = []
responses = []

# Extract patterns and responses
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        responses.append(random.choice(intent["responses"]))

# Text preprocessing
def preprocess(text):

    tokens = nltk.word_tokenize(text.lower())

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(tokens)

# Process patterns
processed_patterns = [
    preprocess(pattern)
    for pattern in patterns
]

# TF-IDF
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(
    processed_patterns
)

# Response function
def chatbot_response(user_input):

    processed_input = preprocess(user_input)

    input_vector = vectorizer.transform(
        [processed_input]
    )

    similarity = cosine_similarity(
        input_vector,
        tfidf_matrix
    )

    best_match_index = similarity.argmax()

    best_score = similarity[0][best_match_index]

    if best_score < 0.2:
        return "Sorry, I don't understand."

    return responses[best_match_index]