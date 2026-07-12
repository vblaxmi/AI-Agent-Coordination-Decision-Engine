from agents.coordinator_agent import CoordinatorAgent


class EnterpriseWorkflow:

    def __init__(self):
        self.coordinator = CoordinatorAgent()

    def run(self, business_request):
        return self.coordinator.execute(business_request)