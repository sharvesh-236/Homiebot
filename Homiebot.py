def chatbot():
    print("Welcome to Study homie Bot!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        if user in ["hi", "hello", "hey"]:
            print("Bot: Hello! Welcome to Study homie Bot.")

        elif user == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user == "what can you do":
            print("Bot: I can give study tips and answer simple predefined questions.")

        elif user == "python":
            print("Bot: Python is a beginner-friendly programming language.")

        elif user == "motivate me":
            print("Bot: Believe in yourself. Keep learning every day!")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()