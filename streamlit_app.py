import streamlit as st
import random 

st.title("Cat Laughs!")
st.write(
    "A random joke generator for your enjoyment! "
)
st.image("cat.webp")
###Copilot 
# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the math book look sad? Because it had too many problems.",
    "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call fake spaghetti? An impasta!"
]

# Function to get a random joke
def get_random_joke():
    return random.choice(jokes)

# Streamlit app
st.title('Random Joke Generator')

if st.button('Tell me a joke!'):
    joke = get_random_joke()
    st.write(joke)

