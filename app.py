import streamlit as st
import openai

# --- Configuration ---
st.set_page_config(page_title="PhysicsPal - DP Physics Assistant", layout="wide")
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Store your key in Streamlit secrets

# --- App Header ---
st.title("🧪 PhysicsPal - Your DP Physics Assistant")
st.markdown("""
Welcome to **PhysicsPal** — your personal AI assistant for DP Physics (2025 syllabus).
Ask questions, get explanations, IA ideas, or review help anytime.
""")

# --- Sidebar Instructions ---
st.sidebar.header("Instructions")
st.sidebar.markdown("""
- Ask about any DP Physics topic
- Use IB command terms (e.g., *explain*, *derive*)
- Try: *"Suggest a physics IA on circular motion"*  
- Or: *"Generate 5 MCQs on thermal physics"*
""")

# --- User Input ---
query = st.text_area("Enter your physics question or request below:", height=150)
submit = st.button("Ask PhysicsPal")

# --- System Prompt ---
system_prompt = """
You are PhysicsPal, an expert AI tutor trained to help students with DP Physics (2025 syllabus).
- Always respond using IB command terms when relevant.
- Align answers with the DP curriculum.
- Offer deep yet accessible explanations.
- Encourage critical thinking and conceptual clarity.
- If asked for an IA idea, suggest safe, feasible, and original topics.
- If asked for practice, generate relevant multiple choice or structured questions.
- Include TOK or Nature of Science connections when prompted.
"""

# --- API Call ---
if submit and query:
    with st.spinner("PhysicsPal is thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ]
            )
            answer = response['choices'][0]['message']['content']
            st.markdown("### 📘 Response")
            st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Enter a question or command and click the button above.")

# --- Footer ---
st.markdown("---")
st.caption("Powered by OpenAI | Built for the IB DP Physics curriculum")
