import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from knowledge_base import get_top_chunks


#Load Groq API key
GROQ_API_KEY=load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# Set Steamlit UI
st.title("RegoGPT")

#Model options
MODEL_OPTIONS = [
    "llama3-8b-8192",
    "qwen-qwq-32b",
    "deepseek-r1-distill-llama-70b"
]
selected_model = st.selectbox("Choose a model:", MODEL_OPTIONS)

# User input
user_prompt = st.text_area("Enter policy description.")


# Generate button
if st.button("Generate Policy"):
    if not user_prompt.strip():
        st.warning("Enter policy description.")
    else:
        with st.spinner("Generating REGO Policy..."):
            # Vector search
             # Use custom vector search (no LangChain)
            relevant_docs = get_top_chunks(user_prompt, k=3)
            context = "\\n\\n".join(relevant_docs)

            full_prompt = f"""
You are RegoGPT, an expert policy author trained on Open Policy Agent (OPA) and Rego language.
Generate a secure, production-ready Rego policy based on the user's request.
Only return valid REGO code. Do not explain anything unless asked.

Relevant Context:
{context}

Policy Description:
\"\"\"
{user_prompt}
\"\"\"
"""

            chat_completion = client.chat.completions.create(
                model=selected_model,
                messages=[
                    {"role": "system", "content": full_prompt},
                ],
                temperature=0.3
            )
            output = chat_completion.choices[0].message.content.strip()
            st.subheader("🧾 Generated REGO Policy:")
            st.code(output, language="rego")
            st.session_state["generated_rego"] = output

# Optional: Explanation feature
if "generated_rego" in st.session_state and st.button("Explain Policy"):
    with st.spinner("Explaining the policy..."):
        explanation_prompt = f"Explain this REGO policy in details:\n\n{st.session_state['generated_rego']}"
        explanation = client.chat.completions.create(
            model=selected_model,
            messages=[
                {"role": "system", "content": "You are a Rego policy expert who explains code simply."},
                {"role": "user", "content": explanation_prompt}
            ],
            temperature=0.1
        )
        st.subheader("📘 Explanation:")
        st.write(explanation.choices[0].message.content.strip())
