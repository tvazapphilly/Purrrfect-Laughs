import streamlit as st
import random 
import requests

# title 
st.title("Cat Laughs!")
# site description
st.write(
    "A random joke generator for your enjoyment! "
)
st.image("cat-cats.gif")

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
=======
primaryColor = '#7792E3'
backgroundColor = '#E6E6FA'  # Light purple color
secondaryBackgroundColor = '#ffffff'
textColor = '#333333'
font = "sans serif"


# Fetch joke function (without caching)
def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
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

