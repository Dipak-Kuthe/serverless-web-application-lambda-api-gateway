import json
import os
from datetime import datetime, timezone


def lambda_handler(event, context):
    name = event.get("queryStringParameters") or {}
    visitor = name.get("name", "DevOps learner")

    body = {
        "message": f"Hello, {visitor}!",
        "service": os.getenv("AWS_LAMBDA_FUNCTION_NAME", "local"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
