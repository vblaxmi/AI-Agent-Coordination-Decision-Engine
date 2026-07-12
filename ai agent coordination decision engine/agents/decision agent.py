from langchain_openai import ChatOpenAI
from prompts.templates import DECISION_PROMPT

class DecisionEngine:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini")

    def decide(self, hr, finance, operations):

        prompt = DECISION_PROMPT.format(
            hr=hr,
            finance=finance,
            operations=operations
        )

        return self.llm.invoke(prompt).content
