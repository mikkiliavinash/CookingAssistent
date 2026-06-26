# 🍳 Chef Buddy – AI Cooking Assistant

Chef Buddy is an AI-powered cooking assistant built using **LangChain**, **Google Gemini**, **Streamlit**, and **Tavily Search**. 
It helps users discover recipes, find ingredient substitutions, learn cooking techniques, and receive practical cooking guidance through a conversational interface.

The application uses Google Gemini as the language model and Tavily Search to retrieve current cooking-related information when needed. 
It also maintains conversation context using LangGraph's in-memory checkpointing.

---

## 🚀 Live Demo

**Streamlit App:** https://cookingassistent-avinashmikkili.streamlit.app/

---

## 📂 GitHub Repository

mikkiliavinash/CookingAssistent

---

## ✨ Features

* 🍳 AI-powered cooking assistant
* 🥗 Suggests recipes based on available ingredients
* 🔄 Recommends affordable ingredient substitutions
* 🔍 Uses Tavily Search for up-to-date cooking information
* 💬 Conversational chat interface built with Streamlit
* 🧠 Maintains conversation context using LangGraph InMemorySaver
* 🚫 Politely refuses non-cooking related questions
* 📱 Simple and responsive web interface

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### AI Framework

* LangChain
* LangGraph

### Large Language Model

* Google Gemini 2.5 Flash

### Search Tool

* Tavily Search API

### Environment Management

* Python Dotenv

### Programming Language

* Python 3.12+

---

## 📁 Project Structure

```text
CookingAssistent/
│
├── app.py                # Streamlit application
├── agent.py              # LangChain agent configuration
├── prompts.py            # System prompt
├── tools.py              # Tavily search tool
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone mikkiliavinash/CookingAssistent
```

Go to the project directory:

```bash
cd CookingAssistent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

For Streamlit Community Cloud, add these keys using **App Settings → Secrets** instead of uploading the `.env` file.

---

## ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

## 👨‍💻 Author

**Avinash Mikkili**

GitHub: https://github.com/mikkiliavinash
