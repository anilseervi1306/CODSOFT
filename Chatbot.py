def chatbot(input_text):
    if "hello" in input_text.lower():
        return "Hello! how can i help you?"
    elif "how are you" in input_text.lower():
        return "I'm fine but I am just a bot and i am here to help you!"
    elif "goodbye" in input_text.lower():
        return "Goodbye! have a great day!"
    elif "what is your name" in input_text.lower():
        return "I am sara"
    else:
        return "I'm sorry, I didn't understand what you are saying"

# Main program
print("Welcome to Simple Chatbot! Type 'exit' to end the conversation")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    else:
        response = chatbot(user_input)
        print("Chatbot:", response)
