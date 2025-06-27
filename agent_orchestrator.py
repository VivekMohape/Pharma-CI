import os
from typing import Dict, Any
import openai
from openai import OpenAI

class AgentOrchestrator:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found. Please enter it in the UI.")
        
        self.client = OpenAI(api_key=api_key)

    def run(self, input_text: str) -> Dict[str, Any]:
        summary = self.generate_summary(input_text)
        competitors = self.extract_competitors(input_text)
        clinical_trials = self.mock_clinical_trials(input_text)

        return {
            "executive_summary": summary,
            "competitor_insights": competitors,
            "clinical_trials": clinical_trials,
            "raw_input": input_text
        }

    def generate_summary(self, text: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the following pharma press release."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()

    def extract_competitors(self, text: str) -> list:
        keywords = ["Pfizer", "Moderna", "Novartis", "Roche"]
        return [k for k in keywords if k.lower() in text.lower()]

    def mock_clinical_trials(self, text: str) -> list:
        return [
            {"trial": "Phase 2 - ABC123", "status": "Recruiting"},
            {"trial": "Phase 3 - XYZ789", "status": "Completed"}
        ]
