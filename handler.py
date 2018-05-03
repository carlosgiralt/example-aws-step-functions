from random import randint


def random_number(event, context):

    number = randint(1, 10)

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "number": number,
        "input": event
    }


def print_input(event, context):
    number = event.get("number", 0)
    return {
        "parity": "even" if number % 2 == 0 else "odd",
        "number": number
    }
