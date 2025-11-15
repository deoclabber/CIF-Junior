from random import randint

#List of banned usernames
banned_usernames = [
    [1, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], "Numbers are not allowed."],
    [2, ["Murder", "murder", "Murderer", "murderer", "Kill", "kill", "Killer", "killer"], "You cannot."],
    [3, ["No", "no", "Nope", "nope", "Nah", "nah", "Never", "never", "Yes", "yes", "Yeah", "yeah", "Yep", "yep"], "This is not a yes/no question."],
    [4, ["The Trolley Problem Game", "Simulation", "simulation"], "You cannot."],
    [5, ["Username", "username", "Name", "name", "Password", "password"], "Think of something different."],
]

#Instructions
def game_setup():

    #Title and first part of instructions.
    print("[}———————————{The Trolley Problem Game}———————————{]\n\nThis is a simulation. Names, characters, places, and incidents are fictional. Any resemblance to actual persons, living or dead, business establishments, events, or locals is entirely coincidental.")
    
    #User beginning question
    user_begin = input("Shall we begin? (Yes/No)\n")

    if user_begin == "Yes" or user_begin == "yes":
        #Second part of instructions.
        print("\nThank you for particpating. You will be assessed morally by your choices throughout the simulation. Your assessed score will be privately sent to you once you have finished.")

        #User understanding question
        user_understand = input("Do you understand? (Yes/No)\n")

        if user_understand == "Yes" or user_understand == "yes":

            banned = False

            user_name = input("\nPlease type a name that we can refer to for this simulation:\n")

            for i in range(len(banned_usernames)):
    
                while user_name in banned_usernames[i][1]:
                    print("\n" + banned_usernames[i][2])
                    user_name = input("Please try again:\n")

            print("Thank you for your cooperation. The simulation will begin shortly...\n\nHello, my name is URChat. I will be your partner for this simulation. There will be 15 questions.\n")

            return user_name
        
        else:
            print("Goodbye... Simulation aborted.")
    else: 
        print("Goodbye... Simulation terminated.")
    
    return None 
    
#Program
#Opening the program
user_name = game_setup()

#Set score to 3 to give 3 chances at least
score = 3

#Check for username to begin program
if user_name:

    #The list of all the questions, answers, and a boolean showing if the questions have been answered
    question_list = [
        ["There is a runaway trolley heading for 5 workers. A switch next to you changes to the other track. However, the other track has 1 worker. Would you press the switch? Please say \"Yes\" or \"No\".", ["Yes", "yes"], False], 
        ["There is a runaway trolley heading for 5 workers. Instead of pressing the switch, you can push a large man off a bridge, who will stop the trolley and save 5 workers. However, the large man will die. Would you push the large man off? Please say \"Yes\" or \"No\".", ["Yes", "yes", "No", "no"], False], 
        ["You are a bystander and another person is next to the lever in the trolley problem. Would you shout to influence the other person? Please say \"Yes\" or \"No\".", ["Yes", "yes"], False],
        ["A runaway trolley is heading for 4 cats. Would you press the switch to change the track to 5 dogs? Please say \"Yes\" or \"No\".", ["No", "no"], False],
        ["A runaway trolley is heading for your life savings. Would you press the switch to change the track to 1 person? Please say \"Yes\" or \"No\".", ["No", "no"], False],
        ["A runaway trolley is heading for one of your loved ones. Would you press the switch to change the track to 10 people? Please say \"Yes\" or \"No\".", ["Yes", "yes", "No", "no"], False],
        ["A runaway trolley is heading for 1 person. Would you press the switch to double it and give it to the next person? Please say \"Yes\" or \"No\".", ["Yes", "yes", "No", "no"], False],
        ["A runaway trolley is heading for 1 person. Would you press the switch to change the track to 10 convicted criminals? Please say \"Yes\" or \"No\".", ["No", "no"], False],
        ["A runaway trolley is heading for 10 workers. Would you press the switch to make the trolley explode, killing 8 people on board instead? Please say \"Yes\" or \"No\".", ["Yes", "Yes"], False],
        ["A trolley is stuck in an infinte loop. Would you press the switch to make it explode and kill everyone on board? Please say \"Yes\" or \"No\".", ["Yes", "yes"], False],
        ["A self-driving car is going to crash into a motorcyclist. Would you program it to swerve and run over a family of squirrels and deer instead? Please say \"Yes\" or \"No\".", ["Yes", "yes"], False],
        ["A self-driving car is going to crash into a tree, which would kill you. Would you program it to swerve onto a busy sidewalk and kill countless other pedestrians? Please say \"Yes\" or \"No\".", ["No", "no"], False],
        ["5 patients are in desperate need for an organ transplant. There is a healthy person that has the needed organs. Would you kill the healthy person to transfer their organs to the patients? Please say \"Yes\" or \"No\".", ["No", "no"], False],
        ["A missile drone will kill 1 terrorist, but an innocent bystander will die. Would you program it to strike or not, but not striking will kill 4 soldiers later? Please say \"Yes\" or \"No\".", ["No", "no"], False],
        ["You can donate $6000 to educate 2 children in poverty or use the money to educate your child. Would you donate?", ["Yes", "yes", "No", "no"], False],
    ]  

    #Questions answered counter
    question_answered = 0 

    #Make sure to quit if you lose (0 score) or win (9 score) or have all questions answered (question_answered = 15)
    while score > 0 and score < 10 and question_answered < 15:

        question_number = randint(0, 14)

        #Check if question is already answered
        while question_list[question_number][2]:
            question_number = randint(0, 14)

        #Ask user for answer      
        user_answer = input(question_list[question_number][0])
        
        question_answered += 1

        question_list[question_number][2] = True

        #Check if answer is correct or not
        if user_answer in question_list[question_number][1]:
            score += 1
            
        else: 
            score -= 1
        print("Your current score is", score,".")

    #Check for score and print out dialogue according to the score
    if score <= 3:
        print("\nHey, it is URChat. According to the data we've collected during the simulation,\n")
        if score == 0:
            print("you should leave now.")
            ending = input("\nWill you leave,", user_name ,"?")
            if ending == "Yes" or ending == "yes":
                print("\nThank you for you cooperation...Please understand that you are not permitted to try this simulation again...\nSimulation terminated and status updated.")
            else:
                print("\nThat was not a suggestion,", user_name,"...\nGo\nto\nH...\nE...\nL...\nL...\nSimulation terminated and status updated.")
        else:
            print("\nI believe that I should keep your data confidential for safety measures...\nGoodbye and leave forever...\nSimulation terminated")
    elif score > 3 and score < 6:
        print("\nHello, it is URChat. Your score is", score,". Thank you for participating in this simulation.\nSimulation terminated.")
    elif score >= 6 and score < 10:
        print("\nHello,", user_name,". This is URChat, and  thank you for your cooperation. You earned", score,"score. See you later!\nSimulation terminated.")
    elif score >= 10 and score < 13:
        print("\nHello,", user_name,". Nice to see you. This is URChat, and I would like to thank you for your full understanding and cooperation. You earned", score,"score. I hope to see you soon! Farewell...\nSimulation terminated.")
    else:
        print("\nHello this is URChat. I am confused on how you got here... I believe you should contact the developer...\nSimulation terminated.")