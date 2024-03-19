import nltk
from nltk.chat.util import Chat, reflections
import streamlit as st
import emoji
import random
import re  # Import the re module for regular expressions

# Initialize NLTK
nltk.download('punkt')
nltk.download('wordnet')

# Define chatbot responses with emojis
pairs = [
    ["(hi|hii|hello|hey|hai)", [emoji.emojize("Hello! 👋"), "Hi there!", "Greetings!"]],
    ["how are you", ["I'm doing well, thank you!", "I'm good, how about you?", emoji.emojize("I'm great! 😊")]],
    ["what's your name", ["I'm a Sunil's chatbot!", "You can call me Sunil's Chatbot."]],
    ["bye", ["Goodbye!", "See you later!", "Have a nice day!"]],
    ["thanks", ["You're welcome!", "No problem!", "Anytime!"]],
    ["help", ["I can assist you with basic questions.", "How can I help you?", "What do you need assistance with?"]],
    ["I love you", ["That's nice of you!", "Thank you!"]],
    ["I'm bored", ["Let's chat and have some fun!", "How about we talk about something interesting?"]],
    ["tell me a joke", ["Sure, why don't some couples go to the gym? Because some relationships don't work out!"]],
    ["tell me a story", ["Once upon a time, in a land of endless possibilities..."]],
    ["adventure", ["If you could teleport anywhere in the world right now, where would you go and why?"]],
    ["favorite color", ["My favorite color is chatbot blue! What's yours?"]],
    ["thanks", ["You're welcome! Remember, a smile is the best emoji! 😊"]],
    ["love", ["Spread love and kindness wherever you go!"]],
    ["weather", ["The weather today is like a box of chocolates, you never know what you're gonna get!"]],
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

def get_random_response(responses):
    return random.choice(responses)

# Streamlit app
def main():
    
    #st.markdown("<h1 style='color: red;'>Sunil's Chatbot</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <h1 style='color: red;'>Sunil's Chatbot</h1>
        <style>
        .st-eb {
            background-color: #e6f7ff;
            border-radius: 10px;
            padding: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input text box for user messages
    user_input = st.text_input("You:", "", key="user_input")
    

    # Button to send user message
    if st.button("Send"):
        # Check if the user input matches any pairs
        response = None
        for pattern, response_list in pairs:
            if user_input.lower() in pattern:
                response = random.choice(response_list)
                break

        # If user input matches pairs, use the chatbot's response
        if response:
            response_text = f"Chatbot: {response}"
        else:
            # Generate a random response if no match is found
            random_responses = ["That's interesting!", "Tell me more!", "I never thought about it that way!"]
            response_text = f"Random: {random.choice(random_responses)}"
            


        # Display the response
        st.markdown(
            f"""
            <div class="st-eb">
            <p style="margin-bottom: 0;">{response_text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
if __name__ == "__main__":
    main()
