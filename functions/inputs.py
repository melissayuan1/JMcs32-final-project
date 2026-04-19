def get_valid_input(prompt, valid_options):
    while True:
        choice = input(prompt).lower() #lower case so that capitlization does not impact
        if choice in valid_options: #iterates through to check if valid choice
            return choice #returns if yes
        print(f"Invalid. Choose from: {', '.join(valid_options)}") #if not prints invalid + options and let's user enter again


def get_float(prompt): #used in guess32.py
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")
