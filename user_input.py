def get_input(input_message, validator, invalid_message):
    while True:
        user_input = input(input_message)

        if(validator(user_input)):
            break

        print(invalid_message)

    return user_input