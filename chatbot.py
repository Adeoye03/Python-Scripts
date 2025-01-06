def chatbot():
    print("Hello! i'm your AI chatbot. How can i assist you today?")
    while True:
        user_input = input("You:").lower()

        if "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hi there! How can i help you?")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "your name" in user_input:
            print("Chatbot: i'm a simple AI chatbot, still learning new things!")
        else:
            print("Chatboy: i'm not sure how to respond to that. Can you ask something else?")


chatbot()