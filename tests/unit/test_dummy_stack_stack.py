import aws_cdk as core
import aws_cdk.assertions as assertions

from dummy_stack.dummy_stack_stack import DummyStackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dummy_stack/dummy_stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DummyStackStack(app, "dummy-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
