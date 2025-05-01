# 🔐 RegoGPT

**RegoGPT** is an AI-powered Rego policy generator that translates natural language prompts into valid, production-grade Rego policies for use with [Open Policy Agent (OPA)](https://www.openpolicyagent.org/). It uses Groq-hosted LLMs and a custom document retrieval system to generate policies. 

---

## 🚀 Features

- Description of the policy to Rego conversion
- 3 LLM model selections: LLaMA 3, DeepSeek, Qwen
- Context-aware policy generation using real Rego docs
- Policy explanation feature
---

## 📁 Folder Structure

```
RegoGPT/
├── app.py                  # Streamlit frontend
├── knowledge_base.py       # Embedding + cosine similarity-based doc retriever
├── .env.example            # Example Groq API key format
├── rego_data/
│   ├── opa_docs.txt        # Rego language patterns & OPA basics
│   └── rego_data.txt       # Real Rego policy examples (AWS, GCP, K8s)
```

---

## ⚙️ Getting Started

### 1. Clone the repo and install dependencies

```bash
pip install -r requirements.txt
# Or manually:
pip install streamlit sentence-transformers scikit-learn python-dotenv groq
```

### 2. Add your Groq API key
Get your Groq API Keys here: https://console.groq.com/home
Create a `.env` file in the root:

```
GROQ_API_KEY=your-groq-api-key-here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Visit: [http://localhost:8501](http://localhost:8501)

---

## ✍️ Example Prompts

- `Deny users who do not have MFA enabled`
- `Restrict access from South Korea, China, and Iraq`
- `Only allow root login from internal IPs`
- `Ensure all Kubernetes pods run as non-root`

---

## 🌐 Roadmap

- Coming soon: Add `opa eval` integration to test policies
---

## 👩🏽‍💻 Built by Bina

Security + AI = 🔐💡
