import streamlit as st
import random 
import requests

# title 
st.title("Cat Laughs!")
# site description
st.write(
    "A random joke generator for your enjoyment! "
)
st.image("cat.webp")

### Copilot 
# List of jokes
#jokes = [
#    "Why don't scientists trust atoms? Because they make up everything!",
#    "Why did the math book look sad? Because it had too many problems.",
#    "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
#    "Why did the scarecrow win an award? Because he was outstanding in his field!",
#    "What do you call fake spaghetti? An impasta!"
#]

# Function to get a random joke
#def get_random_joke():
#    return random.choice(jokes)

# Streamlit app
#st.title('Random Joke Generator')

#if st.button('Tell me a joke!'):
#    joke = get_random_joke()
#    st.write(joke)
# Fetch joke function (without caching)

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    try:
        response = requests.get(url)
        joke = response.json().get("joke", "Oops! No joke found.")
        return joke
    except Exception as e:
        return f"Error fetching joke: {e}"

# Streamlit app
if st.button('Tell me a joke!'):
    joke = fetch_joke()
    st.write(joke)

def fetch_programmingjoke():
    url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    try:
        response = requests.get(url)
        joke = response.json().get("joke", "Oops! No joke found.")
        return joke
    except Exception as e:
        return f"Error fetching joke: {e}"


# Categorize Jokes
st.header("Optional Customization")
st.subheader("Choose a Category!")
if st.button("Programming"):
    joke = fetch_programmingjoke()
    st.write(joke)



