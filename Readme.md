# 🤖 AI Research Copilot

This project is an intelligent AI-based research assistant that can answer questions using multiple data sources like PDFs, web search, and local notes.

Instead of relying on a single source, the system uses an agent to decide where to fetch the best information from. This makes the responses more accurate and context-aware.

---

## 💡 What this project does

- You can ask any question related to AI, ML, NLP, etc.
- The system decides whether to:
  - search in a PDF
  - search on the web
  - use local notes
- It then combines the information and generates a final answer using an LLM

---

## ⚙️ Tech Stack

- Python  
- LangChain (for agent + RAG pipeline)  
- ChromaDB (vector database)  
- Groq API (LLM)  
- Tavily API (web search)  
- HuggingFace Embeddings  
- Streamlit (UI)

---

## 🧠 How it works (simple)

1. User enters a query
2. Agent analyzes the question
3. Agent selects the best tool:
   - PDF search
   - Web search
   - Text search
4. Relevant data is retrieved
5. LLM generates the final answer

---

## 📁 Project Structure


agentic-rag-project/
│── app.py
│── agent.py
│── tools/
│ ├── pdf_tool.py
│ ├── web_tool.py
│ ├── text_tool.py
│── data/
│ ├── docs.pdf
│ ├── notes.txt
│── requirements.txt
│── .env


---

## 🚀 How to run

1. Clone the repo  
2. Create virtual environment  
3. Install dependencies  

```bash
pip install -r requirements.txt
Add API keys in .env
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
Run the app
streamlit run app.py

🔍 Example questions
What is AI?
Explain Machine Learning
What is RAG?
Latest trends in AI
Explain Agentic AI
📌 What I learned
How RAG systems actually work
How agents select tools dynamically
Working with LLM APIs
Building real-world AI apps using LangChain
Handling errors and debugging agent behavior
🚧 Future improvements
Add chat memory
Improve retrieval accuracy
Add better UI/UX
Deploy as API
👩‍💻 Author

Gunjan Sharma
GitHub: https://github.com/Gunjansharma003

If you found this project useful, feel free to ⭐ the repo 🙂


---

# 💥 Difference (important)

👉 Ye version:
- natural language ✔️  
- simple tone ✔️  
- human-written feel ✔️  
- no over-engineered wording ❌  

---

💬 Agar tu chahe:
👉 main tujhe **GitHub repo description (1-line + tags)** bhi bana dungi  
👉 ya **LinkedIn post** bhi 🚀