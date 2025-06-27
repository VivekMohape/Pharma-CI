import streamlit as st
import os
from src.orchestrator.agent_orchestrator import AgentOrchestrator

# UI Setup
st.set_page_config(page_title="Pharma CI Streamlit", layout="wide")
st.title(" Pharma CI - Multi-Agent Intelligence")

# Ask user for OpenAI API Key
user_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Store it in session and set env var
if user_api_key:
    st.session_state["OPENAI_API_KEY"] = user_api_key
    os.environ["OPENAI_API_KEY"] = user_api_key

    # Initialize orchestrator
    @st.cache_resource
    def get_orchestrator():
        return AgentOrchestrator()

    orchestrator = get_orchestrator()

    # Input text
    user_query = st.text_area("Enter a press release or news snippet", height=300)

    if st.button("Run Analysis"):
        if not user_query.strip():
            st.warning("Please enter some text before running.")
        else:
            with st.spinner("Running multi-agent analysis..."):
                try:
                    result = orchestrator.run(input_text=user_query)
                    st.success("Analysis complete.")
                    st.subheader("Structured Output (JSON)")
                    st.json(result)
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    st.info("Please enter your OpenAI API Key to begin.")
