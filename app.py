import streamlit as st
from openai import OpenAI
import os

# Use secure method to load your API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI
st.title("Gym AI Assistant 💪")
st.subheader("Powered by GPT")

user_input = st.text_input("Share your feelings with me :)")

# Trigger AI response
if user_input:
    st.write("You said:", user_input)

    with st.spinner(" BroGPT is thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a motivational fitness assistant who gives workout advice, tracks mood, and supports users like a virtual coach. You will also be a gym bro"},
                    {"role": "user", "content": user_input}
                ]
            )

            ai_response = response.choices[0].message.content
            st.success("CoachGPT says:")
            st.write(ai_response)

        except Exception as e:
            st.error(f"Oh geez Rick! : {e}")

