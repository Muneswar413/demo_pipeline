import json
from utils import put_contact, get_contact, list_contacts

def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method")
    path = event.get("rawPath")

    if method == "POST" and path == "/contact":
        body = json.loads(event["body"])
        result = put_contact(body)
        return {"statusCode": 200, "body": json.dumps(result)}

    elif method == "GET" and path.startswith("/contact/"):
        name = path.split("/")[-1]
        result = get_contact(name)
        return {"statusCode": 200, "body": json.dumps(result)}

    elif method == "GET" and path == "/contacts":
        result = list_contacts()
        return {"statusCode": 200, "body": json.dumps(result)}

    else:
        return {"statusCode": 404, "body": "Route not found"}

    