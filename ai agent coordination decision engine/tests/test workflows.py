from workflows.workflow import EnterpriseWorkflow


def test_workflow():

    workflow = EnterpriseWorkflow()

    result = workflow.run(
        "Should the company hire 10 new employees for expansion?"
    )

    assert "decision" in result