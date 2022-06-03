from aws_cdk import (
    Duration,
    Stack,
)
from constructs import Construct
import pwed_cdk

class DummyStackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ttl = pwed_cdk.pwed_ttl.Ttl(self, "pwed_ttl",
            ttl=Duration.minutes(5),
            poll_interval=Duration.minutes(1),
        )
