import streamlit as st
import requests

# Set title and description
st.title("Cat Laughs!")
st.write("A random joke generator for your enjoyment!")
st.image("cat.webp")

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
