from  langchain.prompts import PromptTemplate

HR_PROMPT = PromptTemplate(
    input_variables=["query"],
    template="""
You are an HR Specialist Agent.

Analyze the following request and provide HR-related recommendations.

Request:
{query}
"""
)

FINANCE_PROMPT = PromptTemplate(
    input_variables=["query"],
    template="""
You are a Finance Specialist Agent.

Analyze the following request and provide financial recommendations.

Request:
{query}
"""
)

OPERATIONS_PROMPT = PromptTemplate(
    input_variables=["query"],
    template="""
You are an Operations Specialist Agent.

Analyze the following request and provide operational recommendations.

Request:
{query}
"""
)

DECISION_PROMPT = PromptTemplate(
    input_variables=["hr", "finance", "operations"],
    template="""
You are an Enterprise Decision Engine.

Review the recommendations below:

HR:
{hr}

Finance:
{finance}

Operations:
{operations}

Generate a final enterprise decision with justification.
"""
)