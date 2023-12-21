import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

all_list_pictures = [rock, scissors, paper]
all_list = ["Kámen", "Nůžky", "Papír"]


user_choice = str(input('Vyberte si Kámen, Nůžky nebo Papír\n')).lower()
user_choice_num = 0
if user_choice == "kámen":
    user_choice_num += 0 
    user_picture = all_list_pictures[user_choice_num]

    computer_choice = random.randint(0, 2)
    computer_picture = all_list_pictures[computer_choice]
    print(f"Vybral jste si: {str(all_list[user_choice_num])}\n{user_picture}")
    print(f"Počítač si vybral: {all_list[computer_choice]}\n{computer_picture}")

    if user_choice_num == computer_choice:
        print("Remíza")
    elif (user_choice_num == 0 and computer_choice == 2) or (user_choice_num == 2 and computer_choice == 1) or (user_choice_num == 1 and computer_choice == 0):
        print("Prohrál jsi, počítač vyhrál")

    elif (user_choice_num == 0 and computer_choice == 1) or (user_choice_num == 2 and computer_choice == 0) or (user_choice_num == 1 and computer_choice == 2):
        print("Vyhrál jsi, počítač prohrál")

elif user_choice == "nůžky":
    user_choice_num +=1
    user_picture = all_list_pictures[user_choice_num]

    computer_choice = random.randint(0, 2)
    computer_picture = all_list_pictures[computer_choice]
    print(f"Vybral jste si: {str(all_list[user_choice_num])}\n{user_picture}")
    print(f"Počítač si vybral: {all_list[computer_choice]}\n{computer_picture}")

    if user_choice_num == computer_choice:
        print("Remíza")
    elif (user_choice_num == 0 and computer_choice == 2) or (user_choice_num == 2 and computer_choice == 1) or (user_choice_num == 1 and computer_choice == 0):
        print("Prohrál jsi, počítač vyhrál")

    elif (user_choice_num == 0 and computer_choice == 1) or (user_choice_num == 2 and computer_choice == 0) or (user_choice_num == 1 and computer_choice == 2):
        print("Vyhrál jsi, počítač prohrál")

elif user_choice == "papír":
    user_choice_num +=2

    user_picture = all_list_pictures[user_choice_num]

    computer_choice = random.randint(0, 2)
    computer_picture = all_list_pictures[computer_choice]
    print(f"Vybral jste si: {str(all_list[user_choice_num])}\n{user_picture}")
    print(f"Počítač si vybral: {all_list[computer_choice]}\n{computer_picture}")

    if user_choice_num == computer_choice:
        print("Remíza")
    elif (user_choice_num == 0 and computer_choice == 2) or (user_choice_num == 2 and computer_choice == 1) or (user_choice_num == 1 and computer_choice == 0):
        print("Prohrál jsi, počítač vyhrál")

    elif (user_choice_num == 0 and computer_choice == 1) or (user_choice_num == 2 and computer_choice == 0) or (user_choice_num == 1 and computer_choice == 2):
        print("Vyhrál jsi, počítač prohrál")

else:
    print("Nemůžete zadat nic jiného než je uvedeno")