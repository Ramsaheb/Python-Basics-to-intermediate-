# MY PROGRAMM 

# print("\"What is the color of mango at its base state\"")

# def ans():
#     if choice == 1:
#         return "\n Yoohoo you nailed it!!"

# while True:
#     print("1. Green ")
#     print("2. Yellow ")
#     print("3. White ")
#     print("4. Red ")

#     choice = int(input(" What option do you think that is correct: "))

#     print(ans())


# TAKING HELP 

import random

def kbc_game():
    questions = [
        "What is the capital of France?",
        "Who wrote 'Romeo and Juliet'?",
        "What is the chemical symbol for water?",
        "Who painted the Mona Lisa?",
        "What is the largest mammal?",
    ]
    options = [
        ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
        ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
        ["A. H2O", "B. CO2", "C. O2", "D. NaCl"],
        ["A. Pablo Picasso", "B. Leonardo da Vinci", "C. Vincent van Gogh", "D. Michelangelo"],
        ["A. Elephant", "B. Blue whale", "C. Giraffe", "D. Gorilla"],
    ]
    answers = ['B', 'A', 'A', 'B', 'B']
    money = [1000, 2000, 3000, 5000, 10000]

    total_money = 0

    for i in range(len(questions)):
        print("\nQuestion", i+1, ":", questions[i])
        for option in options[i]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == answers[i]:
            print("Correct Answer!")
            total_money += money[i]
            if total_money == 10000:
                print("\nCongratulations! You've won the game!")
                break
            else:
                print("You won Rs.", money[i])
                print("Total Money won so far: Rs.", total_money)
        else:
            print("Incorrect Answer! Game Over!")
            break

kbc_game()
