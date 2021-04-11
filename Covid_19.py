# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:45:55 2021
​
@author: Elif & Zeynep
"""
while True:
    age = input("Please input your age: ")
  # <--- Begining of the numeric control --->  
    try:  
        
        if not age:
            print("Age can't be blank")
        age = int(age)
        if age < 0:
            print("Please input a valid age")
            continue
        elif 0 < age <75:
            age = False
        elif 75 <= age < 100:
            age = True
        else:
            print("Please input a valid age!!!")
            continue             
    except ValueError:
        print("Please input your age as numeric")
        continue
    # <--- End of the numeric control --->
    
    chronicle = input("Do you have a severe chronic disease? Yes or No : ")
    if not chronicle:
        print("Please, answer, can't be blanked")
    elif chronicle.lower() == "yes":
        chronicle = True
    elif chronicle.lower() == "no":
        chronicle = False
    else:
        print("Please write your answer. As Yes or No ")
        continue
    
    immune = input("Is your immune system too weak? Yes or No: ")
    if not immune:
        print("Please, answer, can't be blanked")
    elif immune.lower() == "yes":
        immune = True
    elif immune.lower() == "no":
        immune = False
    else:
        print("Please write your answer. As Yes or No")
        continue
    
    if age and immune and chronicle:
        print("You are in group of High Risk Death!!! Wear a Mask! Save Your Life! ")
    elif age and immune or age and chronicle or immune and chronicle:
        print("You are in medium risk group. Please keep on wearing a mask!")
    else:
        print("You are not in Risk Group but wear a mask and keep social distance")