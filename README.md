# 🧠 Modular Agentic AI Chatbots

This project showcases three modular AI chatbot systems built using **LangChain**, **LangGraph**, **Streamlit**, and **Groq-provided LLMs**, all managed in a modern `uv` Python workspace using `pyproject.toml`.

![Modular Agentic AI Chatbots](./cb762be9-b5c2-44ac-b0ad-c84e8cae452d.png)

---

## 📦 Project Modules

### 1. **Basic Chatbot**
A foundational chatbot powered by Groq-hosted LLMs. Handles simple conversational flows without external tools.

- ✅ Blazing-fast Groq inference
- 💬 Dialog-only logic
- 🧼 Clean, minimal setup

---

### 2. **Chatbot with Tools**
A more advanced chatbot that uses LangGraph to decide when to call external tools (e.g., calculator, search) based on the user's input.

- 🛠 Tool-based reasoning
- 🔄 Groq + LangGraph orchestration
- 🧠 Decision-based tool selection

---

### 3. **AI News Summarizer (AI in Aviation)**
An agent pipeline that fetches real-time **AI in aviation** news via an API, summarizes the results using Groq, and stores the output.

- ✈️ Domain-specific (AI in aviation)
- 🌐 API-powered content fetching
- 🧠 LLM summarization with Groq
- 💾 Local result saving
- 🔁 Continuous agentic loop

---

## ⚙️ Tech Stack

- **LangChain** – LLM orchestration
- **LangGraph** – Agent graph building
- **Groq LLMs** – Ultra-low latency inference
- **Streamlit** – UI interface
- **uv + pyproject.toml** – Modern Python package & workspace management

---

## 🚀 Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/your-username/agentic-chatbots.git
cd agentic-chatbots





