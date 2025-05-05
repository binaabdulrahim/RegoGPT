# RegoGPT

RegoGPT is an AI-powered Rego policy generator that translates natural language prompts into valid, production-grade Rego policies for use with Open Policy Agent (OPA). It uses Groq-hosted LLMs and a custom document retrieval system to generate policies.

# OPA
OPA stands for Open Policy Agent, an open-source policy engine maintained by Styra and a community of contributors. Just like Terraform is the standard tool for building infrastructure (a.k.a. Infrastructure as Code), think of OPA as the one-stop shop for defining and enforcing policies using code — also known as Policy as Code (PaC).

# Rego
Rego is the policy language used by OPA to define rules. It is a declarative, JSON/YAML-based language used to write security and compliance policies — much like how HCL is used to define infrastructure in Terraform.

# Why Use Rego to Write Policies?
A policy is simply a set of conditions or statements that define what is allowed or denied. Rego (the language) is used with OPA (the engine) to consistently apply the same policy logic across various platforms like Terraform, Kubernetes, microservices, and more. In addition, OPA evaluates policies in real time, and Rego makes this possible by being a flexible, testable, and interoperable language that works seamlessly across diverse systems.

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

### 1. Set up Virtual Environment 

#### Mac
1. python3 -m venv venv
2. source venv/bin/activate

#### Windows
1. python3 -m venv venv
2. venv/Scripts/activate
   
### 2. Clone the repo and install dependencies

```bash
pip install -r requirements.txt
# Or manually:
pip install streamlit sentence-transformers scikit-learn python-dotenv groq
```

### 3. Add your Groq API key
Get your Groq API Keys here: https://console.groq.com/home

Create a `.env` file in the root:

```
GROQ_API_KEY=your-groq-api-key-here
```

---

### 4. Run the App

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
