import random

# Predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Greetings!", "How can I help you?"],
    "how are you?": ["I'm just a program, but thanks for asking!", "I'm doing great! How about you?"],
    "what is your name?": ["I'm a chatbot created by you!", "You can call me Chatbot!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
}

def get_response(user_input):
    # Normalize user input to lowercase
    user_input = user_input.lower()
    
    # Check for a matching response
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that."

def chat():
    print("Welcome to Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
