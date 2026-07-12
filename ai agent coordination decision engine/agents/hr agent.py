from langchain_openai import ChatOpenAI
from prompts.templates import HR_PROMPT

class HRAgent:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini")

    def run(self, query):
        prompt = HR_PROMPT.format(query=query)
        return self.llm.invoke(prompt).content