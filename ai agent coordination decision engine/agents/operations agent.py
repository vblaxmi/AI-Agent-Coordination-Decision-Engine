from langchain_openai import ChatOpenAI
from prompts.templates import OPERATIONS_PROMPT

class OperationsAgent:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini")

    def run(self, query):
        prompt = OPERATIONS_PROMPT.format(query=query)
        return self.llm.invoke(prompt).content