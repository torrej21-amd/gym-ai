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
# end of OpenAI Logic

# start of matplot logic
import matplotlib.pyplot as plt
import numpy as np

st.subheader("Mood Tracker")

# Fake data – you can update this later with real user data
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri"])
mood_scores = np.array([6, 7, 5, 8, 9])  # Example: 1-10 mood rating

fig, ax = plt.subplots()
ax.plot(days, mood_scores, marker='o', linestyle='-', color='blue')
ax.set_title("Mood Over the Week")
ax.set_xlabel("Day")
ax.set_ylabel("Mood Level")

st.pyplot(fig)


