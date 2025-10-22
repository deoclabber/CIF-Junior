#Beginning
from random import randint

print("◞୧⎯⎯୨╰ ❝♚Welcome to the number guessing game!♔❞ ╯୧⎯⎯୨◟\n(v1)")

user_replay = "yes"

while user_replay == "yes": 

    #Lower bound and upper bound
    while True:
        lower_bound = int(input("Choose your lower bound: "))
        upper_bound = int(input("Choose your upper bound: "))
        if lower_bound < upper_bound:
            break
        else:
            print("The lower bound must be less than the upper bound. Please try again.")

    #Set user number
    user_number = randint(lower_bound, upper_bound)

    user_try = "yes"

    #Loop to allow multiple tries
    while user_try == "yes":

        user_guess = int(input("Guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ": "))

        #Win or lose
        if user_guess == user_number:
            
            print("𓆩:*¨༺✧꧁𓊈𒆜You Win!𒆜𓊉꧂✧༻¨*:𓆪")

            user_replay = str(input("Do you want to play this game again? (yes/no): "))
            if user_replay != "yes":

                print("-*༺꧁⌋⁋╰* ❝Thank you for trying this game!❞ *╯¶⌊꧂༻*-")
            
            break

        else:

            #Hints
            if user_guess > user_number:
                print("ৡঌৡ ⋆༺𓆩︎Too big!𓆪༻⋆ ৡৡঌ ৡঌ ৡ")
                
            else:
                print("ৡঌৡ ⋆༺𓆩︎Too small!𓆪༻⋆ ৡৡঌ ৡঌ ৡ")

            user_try = str(input("Do you want to try again? (yes/no): "))
            if user_try != "yes":

                user_replay = str(input("Do you want to play this game again? (yes/no): "))
                if user_replay != "yes":

                    print("-*༺꧁⌋⁋╰* ❝Thank you for trying this game!❞ *╯¶⌊꧂༻*-")
