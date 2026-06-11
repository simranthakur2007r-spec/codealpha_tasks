#basic chatbot

def chatbot_reply(user_input):

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."

print("Simple Chatbot")
print("Type 'bye' to end the chat.")

while True:

    user_message = input("You: ").lower()

    reply = chatbot_reply(user_message)

    print("Bot:", reply)

    if user_message == "bye":
        break