from workflows.workflow import EnterpriseWorkflow

workflow = EnterpriseWorkflow()

query = """
The company plans to expand to a new city.
Should we hire 20 employees and increase operations?
"""

result = workflow.run(query)

print("\nHR Recommendation:")
print(result["hr"])

print("\nFinance Recommendation:")
print(result["finance"])

print("\nOperations Recommendation:")
print(result["operations"])

print("\nFinal Decision:")
print(result["decision"])