from agents.hr_agent import HRAgent
from agents.finance_agent import FinanceAgent
from agents.operations_agent import OperationsAgent
from agents.decision_engine import DecisionEngine


class CoordinatorAgent:

    def __init__(self):
        self.hr = HRAgent()
        self.finance = FinanceAgent()
        self.operations = OperationsAgent()
        self.decision_engine = DecisionEngine()

    def execute(self, query):

        hr_result = self.hr.run(query)

        finance_result = self.finance.run(query)

        operations_result = self.operations.run(query)

        final_decision = self.decision_engine.decide(
            hr_result,
            finance_result,
            operations_result
        )

        return {
            "hr": hr_result,
            "finance": finance_result,
            "operations": operations_result,
            "decision": final_decision
        }