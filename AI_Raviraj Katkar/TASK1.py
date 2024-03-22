def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there! How can I help you?"

    elif "how are you" in user_input:
        return "I'm just a chatbot, but thanks for asking!"

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Feel free to come back anytime."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# Example usage:
user_query = input("User: ")
bot_response = simple_chatbot(user_query)
print("Bot:", bot_response)
