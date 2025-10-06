#
from random import randint

random_number = randint(1, 20)

user_guess = int(input("◞୧⎯⎯୨╰ ❝♚Welcome to the number guessing game!♔❞ ╯୧⎯⎯୨◟\n(Beta v0.1) Guess a number between 1 and 20: "))

if user_guess == random_number:
    print("𓆩:*¨༺✧꧁𓊈𒆜You Win!𒆜𓊉꧂✧༻¨*:𓆪")
    
else:
    print("ৡঌৡ ⋆༺𓆩︎You Lose!𓆪༻⋆ ৡৡঌ ৡঌ The correct number was",random_number,"! ৡৡঌৡ")
