# 🤖 Simple Agent — LangChain + Ollama

A simple AI assistant built with **LangChain** and **Ollama** that runs completely locally on your computer.

This project demonstrates how to connect LangChain with a locally running Large Language Model (LLM) using Ollama — **without OpenAI or Gemini API keys**.

---

## ✨ Features

* 🧠 Local AI assistant using Ollama
* 🔗 Built with LangChain
* 💻 Runs completely on your local machine
* 🔑 No API key required
* 💰 No API costs
* 🗣️ Interactive command-line chat
* 🌡️ Configurable model temperature
* 🚪 Simple `exit` / `quit` command
* ⚡ Easy to set up and run

---

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Programming language      |
| LangChain  | LLM application framework |
| Ollama     | Local LLM runtime         |
| Llama 3.2  | Local language model      |

---

## 📁 Project Structure

```text
Simple_agent/
│
├── agent.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

Before running the project, install:

* Python 3.9+
* Ollama
* Git (optional)

### Install Ollama

Download Ollama for Windows:

https://ollama.com/download/windows

After installation, verify it:

```bash
ollama --version
```

---

## 🧠 Download the AI Model

This project uses **Llama 3.2**.

Download the model using:

```bash
ollama pull llama3.2
```

You can test the model with:

```bash
ollama run llama3.2
```

Try asking:

```text
What is Python?
```

To exit Ollama:

```text
/bye
```

---

## 📦 Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd Simple_agent
```

### Create a virtual environment

Using Python:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📄 requirements.txt

The project requires:

```text
langchain
langchain-ollama
```

You can install them directly with:

```bash
pip install langchain langchain-ollama
```

---

## 🚀 Running the Agent

Make sure Ollama is installed and the model is available:

```bash
ollama list
```

You should see:

```text
llama3.2
```

If Ollama is not running, start it with:

```bash
ollama serve
```

Then open another terminal and run:

```bash
python agent.py
```

---

## 💬 Example

The application will display:

```text
============================================================
           SIMPLE LANGCHAIN AI ASSISTANT
============================================================
Ask me anything.
Type 'exit' to stop.

You:
```

Example:

```text
You: What is Python?

Agent:
Python is a high-level, general-purpose programming
language known for its simple syntax and readability.
```

Another example:

```text
You: Explain machine learning in simple words

Agent:
Machine learning is a branch of artificial intelligence
where computers learn patterns from data and use those
patterns to make predictions or decisions.
```

To stop the application:

```text
You: exit

Goodbye!
```

---

## 🔄 How It Works

```text
                User
                  │
                  ▼
            agent.py
                  │
                  ▼
             LangChain
                  │
                  ▼
            ChatOllama
                  │
                  ▼
              Ollama
                  │
                  ▼
             Llama 3.2
                  │
                  ▼
              Response
                  │
                  ▼
                User
```

The application sends the user's question to LangChain.

LangChain communicates with Ollama through `ChatOllama`.

Ollama runs the Llama 3.2 model locally and returns the generated response.

---

## 🔐 API Keys

This project **does not require any API keys**.

You do not need:

```text
OPENAI_API_KEY
GOOGLE_API_KEY
ANTHROPIC_API_KEY
TAVILY_API_KEY
```

The model runs locally through Ollama.

---

## 💰 Cost

**Free to use locally.**

There are no API charges because the LLM is running on your own computer.

> Note: Running a local model uses your computer's CPU/GPU and RAM.

---

## ⚠️ Limitations

Because this project runs a local LLM without external tools:

* It does not perform live web searches.
* It does not automatically access current news.
* It does not retrieve real-time information from the internet.
* The quality of answers depends on the selected local model and your computer's hardware.

For learning LangChain and local LLM development, this provides a simple starting point.

---

## 🔧 Changing the Model

You can use another Ollama model if you have downloaded it.

For example:

```bash
ollama pull qwen2.5:3b
```

Then change the model in `agent.py`:

```python
model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)
```

Make sure the model is installed before running the application.

---

## 📚 Learning Goals

This project helps demonstrate:

* LangChain basics
* Local LLM integration
* Ollama
* `ChatOllama`
* Prompt messages
* LLM invocation
* Python command-line applications
* Running AI models without cloud APIs

---

## 🚀 Future Improvements

Possible improvements include:

* 💾 Conversation memory
* 📄 PDF/document question answering
* 🔍 Retrieval-Augmented Generation (RAG)
* 🛠️ Tool integration
* 🌐 Web search
* 🎨 Streamlit interface
* 🔐 User authentication
* 🧩 Multiple Ollama models

---

## 👩‍💻 Author

**Poornima H B**

BE — Information Science & Engineering

---

## ⭐ Acknowledgements

* [LangChain](https://www.langchain.com/)
* [Ollama](https://ollama.com/)
* Meta's Llama models

---

## 📜 License

This project is intended for **educational and learning purposes**.
