#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 0:
        if count > 0:
            print(count)
        else :
            print("Happy New Year!")
        
        count -=1
happy_new_year()

def square_integers(int_list):
    numberArray=[]
    for num in int_list:
        number= num * num
        numberArray.append(number)
    
    print(numberArray)
square_integers([1, 2, 3, 4, 5])
def fizzbuzz():
    # code goes here!
    i =1
    while i <= 100:
        if (i%3 ==0 and i % 5 !=0):
            print("Fizz")
        elif (i%5 ==0 and i %3 !=0):
            print("Buzz")
        elif (i%5 ==0 and i %3 ==0):
            print("FizzBuzz")
        else :
            print(i)
        i += 1
fizzbuzz()
