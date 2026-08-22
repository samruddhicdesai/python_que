import logging

logging.basicConfig(level=logging.ERROR)


class InvalidInputError(Exception):
    pass


while True:
    try:
        value = input("Enter a positive number or 'quit': ")

        if value == "quit":
            break

        number = int(value)

        if number <= 0:
            raise InvalidInputError("Number must be positive.")

        print("Valid number:", number)

    except ValueError:
        logging.error("User entered a non-numeric value.")
        print("Invalid input.")

    except InvalidInputError as e:
        logging.error(e)
        print(e)