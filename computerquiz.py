#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 2
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 2
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 2
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 2
answer = input("What does KMH stand for? ")
if answer.lower() == "Killo meter per hour":
    print('Correct!')
    score += 2
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct out of 10!")
print("You got " + str((score / 4) * 200) + "%.")


# In[ ]:





# In[ ]:




