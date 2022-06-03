#!/usr/bin/env python3
import os

import aws_cdk as cdk

from dummy_stack.dummy_stack_stack import DummyStackStack


app = cdk.App()
DummyStackStack(app, "DummyStackStack",
    env=cdk.Environment(account='806124249357', region='us-east-1'),
    )

app.synth()
