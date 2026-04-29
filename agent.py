import os
from openai import OpenAI
from prompts import PRD_ANALYSIS_PROMPT, ACCEPTANCE_PROMPT, TESTCASE_PROMPT
from utils import safe_json_load

class PRDAgent:
    def __init__(self, model="gpt-4o-mini"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model

    def _call_llm(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是一个严谨的软件工程专家"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

    def analyze_prd(self, prd_text):
        return safe_json_load(self._call_llm(PRD_ANALYSIS_PROMPT.format(prd=prd_text)))

    def generate_acceptance(self, analysis):
        return safe_json_load(self._call_llm(ACCEPTANCE_PROMPT.format(analysis=analysis)))

    def generate_testcases(self, acceptance):
        return safe_json_load(self._call_llm(TESTCASE_PROMPT.format(acceptance=acceptance)))

    def run(self, prd_text):
        analysis = self.analyze_prd(prd_text)
        acceptance = self.generate_acceptance(analysis)
        testcases = self.generate_testcases(acceptance)
        return {
            "analysis": analysis,
            "acceptance": acceptance,
            "testcases": testcases
        }
