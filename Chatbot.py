import random
import json
import nltk
import spacy
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
nltk.download('punkt')

nlp = spacy.load('en_core_web_sm')

training_data = [
    {"intent": "greeting", "text": "hello"},
    {"intent": "greeting", "text": "hi"},
    {"intent": "greeting", "text": "hey"},
    {"intent": "how_are_you", "text": "how are you"},
    {"intent": "how_are_you", "text": "how's it going"},
    {"intent": "how_are_you", "text": "how are things"},
    {"intent": "i am good", "text": "i am good"},
    {"intent": "i am good", "text": "i am fine"},
    {"intent": "ask", "text": "can i ask about something"},
    {"intent": "ask", "text": "can i know about anything"},
    {"intent": "ask", "text": "i have a questions for you"},
    {"intent": "goodbye", "text": "bye"},
    {"intent": "goodbye", "text": "see you later"},
    {"intent": "goodbye", "text": "goodbye"},
    {"intent": "thanks", "text": "thank you"},
    {"intent": "thanks", "text": "thanks"},
    {"intent": "weather", "text": "how's the weather"},
    {"intent": "weather", "text": "what is the weather like"},
]


responses = {
        "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
        "how_are_you": [" I'm doing great! How about you?"],
        "ask":['yeah sure,Go Ahead',"what do you want to know"],
        "i am good" :["It's glad to hear that"],
        "goodbye": ["Goodbye!", "See you later!", "Take care!"],
        "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
        "weather": ["Let me check the weather for you.", "Fetching the latest weather details..."],
        "default": ["I'm sorry, I didn't understand that.", "Can you rephrase?"]
}

def get_weather(city="kathmandu"):
    api_key = "da799239ed8b4d039b780620250401"  
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"The current temperature in {city} is {temp}°C with {condition}."
    except Exception as e:
        return "Sorry, I couldn't fetch the weather details."

def train_model():
    texts = [item["text"] for item in training_data]
    intents = [item["intent"] for item in training_data]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    model = MultinomialNB()
    model.fit(X, intents)

    return vectorizer, model
def predict_intent(user_input, vectorizer, model):
    X_input = vectorizer.transform([user_input])
    return model.predict(X_input)[0]

def chatbot_response(user_input, vectorizer, model):
    intent = predict_intent(user_input, vectorizer, model)
    
    if intent == "weather":
        return get_weather()  
    else:
        return random.choice(responses.get(intent, responses["default"]))


def chatbot():
    vectorizer, model = train_model()
    print("Chatbot: Hi! I'm your chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input, vectorizer, model)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot()
