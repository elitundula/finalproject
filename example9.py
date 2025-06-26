def risky():
    user_input = "enter a number between 1 and 10: "
    number = int(user_input)
    if number < 1 or number > 10:
        raise ValueError("number must be between 1 and 10")
    print(f"you entered {number}!")

    try:
        risky()
    except ValueError:
        print("you didn't enter a number")

