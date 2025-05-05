# RegoGPT

**RegoGPT** is an AI-powered Rego policy generator that translates natural language prompts into valid, production-grade Rego policies for use with [Open Policy Agent (OPA)](https://www.openpolicyagent.org/). It uses Groq-hosted LLMs and a custom document retrieval system to generate policies. 

# OPA
OPA stands for [Open Policy Agent] (https://www.openpolicyagent.org/), which is an open-source policy engine used 

# Rego

# Why use Rego to make Policies?
A policy is just a set of conditions or statement that define what is aloowed or denied. 

---

## Features

- Description of the policy to Rego conversion
- 3 LLM model selections: LLaMA 3, DeepSeek, Qwen
- Context-aware policy generation using real Rego docs
- Policy explanation feature
---
## Takeway
- The key takeway from this project is that I learned about Groq API, which is a tool that provides free API that streamlines the development process. It also includes up to date LLM models and has one of best documentation. I also had to do some research to understand vectors (embeddings) and cosine similarity. In short, vector embeddings just turns words or sentences into numbers. And cosine similarity is the mesasurment of similarties. Think "dog" and "puppy" which are similiar in meaning so it means it has a high similarity or close to 1. Cosine similarity comes in 3 ranges: 1.0: very similar, 0.0: different, and -1.0: opposite meanings. In order to use turn sentences into numerical embeddings, I utilitzed a Python library called sentence-transformers. 


## Folder Structure

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

## Getting Started

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

## Run the App

```bash
streamlit run app.py
```

Visit: [http://localhost:8501](http://localhost:8501)

---

## Example Prompts

- `Deny users who do not have MFA enabled`
- `Restrict access from South Korea, China, and Iraq`
- `Only allow root login from internal IPs`
- `Ensure all Kubernetes pods run as non-root`

---

## Roadmap

- Coming soon: Add `opa eval` integration to test policies
---

## Built by Bina

Security + AI 
