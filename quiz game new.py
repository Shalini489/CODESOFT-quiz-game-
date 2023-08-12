#!/usr/bin/env python
# coding: utf-8

# In[2]:


# python Quiz game

questions = ("What is the capital of Madhya Pradesh?: ",
                  "Who directed the Avatar movie(2009)?: ",
                  "Which movie won the Academy Award for the best picture in 2020?: ",
                  "How many bones are in the Human body?: ",
                  "Which actor played the role of captain jack Sparrow in the pirates of the Caribbean film series?: ")

options = (("A. Delhi","B. Bhopal","C. Bihar","D. Mumbai"),
                   ("A. Ridley Scott","B. James Cameron","C. Christopher Nolan","D. Steven Spielberg"),
                   ("A. Parasite","B. Once Upon a time in hollywood","C. 1917","D. Joker"),
                   ("A. 206","B. 207","C. 208","D. 209"),
                   ("A. Orlando Bloom","B. keira Knightley","C. Johnny Depp","D. Geoffrey Rush"),)

answers = (("B","B","A","A","C"))
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
print("--------------------")
print("      RESULTS       ")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer,end="")
print()

print("guess: ", end="")
for guess in guesses:
    print(guess,end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is:{score}%")


# In[ ]:




