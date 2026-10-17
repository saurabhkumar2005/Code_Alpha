# Basic Rule-Based Chatbot
# CodeAlpha Python Internship - Task 4

def get_response(message):
    # Convert to lowercase for easy matching
    msg = message.lower().strip()

    # Predefined rules
    if msg in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"
    elif msg in ["how are you", "how are you?", "how's it going"]:
        return "I'm fine, thanks! How about you?"
    elif msg in ["i am fine", "i'm fine", "good", "great"]:
        return "That's wonderful to hear!"
    elif msg in ["what is your name", "who are you"]:
        return "I'm a simple Python chatbot created for CodeAlpha Internship."
    elif msg in ["what can you do", "help"]:
        return "I can chat with you using simple predefined rules. Try saying hello, how are you, or bye."
    elif msg in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    elif msg in ["thanks", "thank you"]:
        return "You're welcome!"
    else:
        return "Sorry, I didn't understand that. Try saying 'hello', 'how are you', or 'bye'."


def main():
    print("=" * 50)
    print("        WELCOME TO BASIC CHATBOT")
    print("=" * 50)
    print("Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()

        # Ignore empty input
        if not user_input:
            continue

        reply = get_response(user_input)
        print(f"Bot: {reply}\n")

        # Exit condition
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()