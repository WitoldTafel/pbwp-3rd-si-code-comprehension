'''
This program selects a rundom number between 1 and 20,
 and asks the user to guess it in less then 6 trys while giving hints every wrong answer
 '''
import random #imports a "random" module
#nothing
guesses_taken = 0# initialize guesses_taken var at value of 0, it is a counter varialbe
#nothing
print('Hello! What is your name?')#prints a string
myName = input()#assign user input to myName varialbe
#nothing
number = random.randint(1, 20)#selects a rundom number between 1 and 20, assign it to "number" varialbe
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')#prints a string with myName value inside it
#nothing
while guesses_taken < 6:#starting while loop with condition based on "guesses_taken" value, it will run until it reach value of 6 or bigger
    print('Take a guess.')#prints a string
    guess = input()#assign user input to guess varialbe
    guess = int(guess)#changes guess var type from str to int
#nothing
    guesses_taken += 1#increases guesses_taken value by 1
#nothing
    if guess < number:#conditional statement, checks if guess value is lower than number value
        print('Your guess is too low.')#prints a string, it runs only if condition above is fulfilled
#nothing
    if guess > number:#conditional statement, checks if guess value is higher than number value
        print('Your guess is too high.')#prints a string, it runs only if condition above is fulfilled
#nothing
    if guess == number:#conditional statement, checks if guess value and number value are equal
        break#terminates while loop, regardless of its condition, it runs only if condition above is fulfilled
#nothing, but we are out of the loop now
if guess == number:#conditional statement, checks if guess value and number value are equal
    guesses_taken = str(guesses_taken)#changes guesses_taken var type from int to str
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')#prints a string with myName and guesses_taken values inside it
#nothing
if guess != number:#conditional statement, checks if guess value and number value are unequal
    number = str(number)#changes guesses_taken var type from int to str
    print('Nope. The number I was thinking of was ' + number)#prints a string with number value at the end
#nothing
