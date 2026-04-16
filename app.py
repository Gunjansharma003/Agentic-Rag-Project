import streamlit as st
from agent import run_agent

# Page config
st.set_page_config(page_title="AI Research Copilot", page_icon="🤖")

# Title
st.title("🤖 AI Research Copilot")

# Description section
st.markdown("## 💡 Ask me questions related to:")
st.markdown("""
- Artificial Intelligence (AI)  
- Machine Learning (ML)  
- Natural Language Processing (NLP)  
- Agentic AI Systems  
""")

st.write("I can search from PDFs, Web, and Notes to give accurate answers 🚀")

# User input
query = st.text_input("🔍 Enter your question:")

# Button click
if st.button("Get Answer"):
    if query:
        with st.spinner("Thinking... 🤔"):
            try:
                response = run_agent(query)
                st.success("✅ Answer generated!")
                st.markdown("### 📌 Answer:")
                st.write(response)
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a question")

# Footer
st.markdown("---")
st.markdown("Built with  using LangChain, Groq, and Streamlit")