# So we are going to create a game of tic tac toe


def user_choice():
    choice = "Wrong"
    acceptable_range = range(0,4+1)
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input("Enter a number between 0 to 4: ")
        if choice.isdigit() == False:
            print("Sorry That is not a digit")

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry , You are out of acceptable range (0-10)")
                within_range = False

    return int(choice)

print(user_choice())

