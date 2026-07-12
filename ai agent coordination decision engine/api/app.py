from fastapi import FastAPI
from pydantic import BaseModel

from workflows.workflow import EnterpriseWorkflow

app = FastAPI(
    title="AI Agent Coordination & Decision Engine"
)

workflow = EnterpriseWorkflow()


class RequestModel(BaseModel):
    query: str


@app.post("/process")
def process_request(request: RequestModel):

    result = workflow.run(request.query)

    return result