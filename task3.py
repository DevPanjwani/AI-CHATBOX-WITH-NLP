import nltk
import random
import string
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample chatbot knowledge base
knowledge_base = """
Hello! I am a simple AI chatbot.
I can answer questions about Python, data science, and internships.
Python is a popular programming language.
Data science involves data analysis and machine learning.
Internships help students gain practical experience.
"""

# Preprocess text
sentences = nltk.sent_tokenize(knowledge_base)
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

def generate_response(user_input):
    user_tokens = preprocess(user_input)
    
    best_match = ""
    max_similarity = 0
    
    for sentence in sentences:
        sentence_tokens = preprocess(sentence)
        similarity = len(set(user_tokens).intersection(sentence_tokens))
        
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = sentence
    
    if max_similarity == 0:
        return "Sorry, I don't understand. Can you rephrase?"
    else:
        return best_match

# Chat loop
print("Chatbot is running. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = generate_response(user_input)
    print("Chatbot:", response)
