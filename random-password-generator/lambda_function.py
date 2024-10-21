import json
import random
import string


def lambda_handler(event, context):
    # Default parameters
    length = 12
    use_letters = True
    use_digits = True
    use_special = True

    # Extract query parameters if provided
    if "queryStringParameters" in event:
        params = event["queryStringParameters"]
        if "length" in params:
            length = int(params["length"])
        if "use_letters" in params:
            use_letters = params["use_letters"].lower() == "true"
        if "use_digits" in params:
            use_digits = params["use_digits"].lower() == "true"
        if "use_special" in params:
            use_special = params["use_special"].lower() == "true"

    # Create the character pool for password generation
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No character types selected"}),
        }

    # Generate random password
    password = "".join(random.choice(char_pool) for _ in range(length))

    # Return the generated password
    return {"statusCode": 200, "body": json.dumps({"password": password})}
