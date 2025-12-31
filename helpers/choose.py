def choose(msg, condition, err="invalid option"):
    while True:
        try:
            print()
            choice = input(msg)
        except ValueError:
            choice = None

        try:
            valid = condition(choice)
        except Exception:
            valid = False

        if valid:
            return choice
        else:
            print(err)
