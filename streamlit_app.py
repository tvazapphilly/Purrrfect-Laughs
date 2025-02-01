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

# Apply custom CSS from an external file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"

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


def fetch_customjoke(category):
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    if category == "programming":
        url = url.replace("Any", "Programming")
    elif category == "misc":
        url = url.replace("Any", "Miscellaneous")
    elif category == "dark":
        url = url.replace("Any", "Dark")
    elif category == "pun":
        url = url.replace("Any", "Pun")
    else:
        url = url
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
    joke = fetch_customjoke("programming")
    st.write(joke)
if st.button("Miscellaneous"):
    joke = fetch_customjoke("misc")
    st.write(joke)
if st.button("Dark Humor"):
    joke = fetch_customjoke("dark")
    st.write(joke)
if st.button("Pun!"):
    joke = fetch_customjoke("pun")
    st.write(joke)
