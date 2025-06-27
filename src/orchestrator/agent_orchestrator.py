import os
from typing import Dict, Any
import openai
import json

class AgentOrchestrator:
    def __init__(self):
        # Ensure the API key is set before use
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found. Please set it via Streamlit UI or .env file.")

        openai.api_key = api_key

    def run(self, input_text: str) -> Dict[str, Any]:
        """
        Main orchestration logic. This is a simplified example that simulates
        multi-agent output. Replace with real agent calls as needed.
        """
        # Simulate multiple agents
        executive_summary = self.generate_summary(input_text)
        competitors = self.extract_competitors(input_text)
        clinical_trials = self.mock_clinical_trials(input_text)

        return {
            "executive_summary": executive_summary,
            "competitor_insights": competitors,
            "clinical_trials": clinical_trials,
            "raw_input": input_text
        }

    def generate_summary(self, text: str) -> str:
        """Uses OpenAI to generate a basic summary."""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the following pharmaceutical press release."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()

    def extract_competitors(self, text: str) -> list:
        """Fake static competitor extraction (replace with NLP or NER)."""
        keywords = ["Pfizer", "Moderna", "Novartis", "Roche"]
        return [k for k in keywords if k.lower() in text.lower()]

    def mock_clinical_trials(self, text: str) -> list:
        """Fake clinical trial stub (can be replaced with real lookup)."""
        return [
            {"trial": "Phase 2 - ABC123", "status": "Recruiting"},
            {"trial": "Phase 3 - XYZ789", "status": "Completed"}
        ]
