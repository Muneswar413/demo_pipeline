def lambda_handler(event, context):
    name = event.get('name', 'krishna')
    age = event.get('age', 35)

    message = f"Hello, my name is {name} and I am {age} years old!"
    print(message)

    return {
        'statusCode': 200,
        'body': message
    }

    