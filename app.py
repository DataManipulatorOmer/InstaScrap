# Import the required modules
import streamlit as st
import instaloader

# Function to fetch and display Instagram profile information
def profilee(username):
    # Create an instance of Instaloader class
    bot = instaloader.Instaloader()

    # Load a profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, username)

    # Display profile information
    st.write("Username:", profile.username)
    st.write("User ID:", profile.userid)
    st.write("Number of Posts:", profile.mediacount)
    st.write("Followers:", profile.followers)
    st.write("Followees:", profile.followees)
    st.write("Bio:", profile.biography)
    st.write("External URL:", profile.external_url)

# Streamlit app layout
def main():
    st.title("Instagram Profile Information")

    # Input field for entering Instagram username
    username = st.text_input("Enter Instagram Username:")

    # Button to fetch and display profile information
    if st.button("Fetch Profile Information"):
        if username:
            profilee(username)
        else:
            st.error("Please enter a valid Instagram username.")

if __name__ == "__main__":
    main()

