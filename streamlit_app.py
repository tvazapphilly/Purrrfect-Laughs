import streamlit as st
import random 
import requests
import streamlit.components.v1 as components
import urllib.parse  # To encode text for sharing


# title 

st.markdown(
    "<h1 style='font-size:48px; font-weight:bold; color:#4c2b75; text-align:center; padding-top:50px;'>Cat Laughs!🐱</h1>", 
    unsafe_allow_html=True
)

# site description

st.markdown(
    "<p style='font-size:35px; font-weight:bold; color:#4c2b75; text-align:center; padding-top:50px; margin-bottom:30px;'>A random joke generator for your enjoyment!</p>", 
    unsafe_allow_html=True
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
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    try:
        response = requests.get(url)
        joke = response.json().get("joke", "Oops! No joke found.")
        return joke
    except Exception as e:
        return f"Error fetching joke: {e}"    

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

# Function to display share buttons
def display_share_buttons(joke):
    encoded_joke = urllib.parse.quote(joke)
    twitter_url = f"https://twitter.com/intent/tweet?text={encoded_joke} 😂 Found this joke on Cat Laughs!"
    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_joke} 😂 Found this joke on Cat Laughs!"
    facebook_url = f"https://www.facebook.com/sharer/sharer.php?u=https://your-app-link.com&quote={encoded_joke}"

    st.markdown("#### Share your joke with your friends! 🎉")
    st.markdown(f"""
        <div style="text-align:center;">
            <a href="{twitter_url}" target="_blank"><button style="background:#1DA1F2;color:white;padding:10px 15px;border:none;border-radius:5px;margin:5px;">🐦 Twitter</button></a>
            <a href="{whatsapp_url}" target="_blank"><button style="background:#25D366;color:white;padding:10px 15px;border:none;border-radius:5px;margin:5px;">📱 WhatsApp</button></a>
            <a href="{facebook_url}" target="_blank"><button style="background:#3b5998;color:white;padding:10px 15px;border:none;border-radius:5px;margin:5px;">📘 Facebook</button></a>
        </div>
    """, unsafe_allow_html=True)

# Generate a random joke
if st.button('Tell me a joke!', key="random_joke"):
    joke = fetch_joke()
    st.write(joke)
    display_share_buttons(joke)

# Categorize Jokes
st.subheader("Or Choose a Category!")

col1, col2 = st.columns(2)

with col1:
    if st.button("Programming", key="prog_joke"):
        joke = fetch_customjoke("Programming")
        st.write(joke)
        display_share_buttons(joke)

    if st.button("Dark Humor", key="dark_joke"):
        joke = fetch_customjoke("Dark")
        st.write(joke)
        display_share_buttons(joke)

with col2:
    if st.button("Miscellaneous", key="misc_joke"):
        joke = fetch_customjoke("Miscellaneous")
        st.write(joke)
        display_share_buttons(joke)

    if st.button("Pun!", key="pun_joke"):
        joke = fetch_customjoke("Pun")
        st.write(joke)
        display_share_buttons(joke)