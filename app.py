import streamlit as st
from openai import OpenAI

# --- Streamlit Page Setup ---
st.set_page_config(page_title="PhysicsPal - DP Physics Assistant", layout="centered")
st.title("🧪 PhysicsPal - Your DP Physics Assistant")

# --- Initialize OpenAI Client ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- Input Box for Student's Prompt ---
user_question = st.text_input("Ask a Physics Question (DP Level):", placeholder="e.g. Explain how interference patterns form in Young's double-slit experiment")

# --- Generate Response ---
if user_question:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that explains DP Physics concepts in simple, clear terms."},
                {"role": "user", "content": user_question}
            ]
        )
        st.markdown("**Answer:**")
        st.write(response.choices[0].message.content)
