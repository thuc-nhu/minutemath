import time
import random

startTime = time.time()
correctCounter = 0
questionCounter = 0
operations = ["+", "-", "*", "/"]

# Get the maximum number for number range
maxNum = int(input("Enter maximum fact family: "))

while time.time() - startTime <= 60:
    # Get the operation
    op = random.choice(operations)

    # Get the two random numbers for the operation (some of this code can be put in a function)
    if op == '/':
        divMax = maxNum * maxNum
        num1 = random.randint(0, divMax)
        num2 = random.randint(1, maxNum)

        while num1 % num2 != 0:
            num2 = random.randint(1, maxNum)

    else:
        num1 = random.randint(0, maxNum)
        num2 = random.randint(0, maxNum)

    # Setting up for answer comparisson
    problem = str(num1) + " " + str(op) + " " + str(num2) + " = "
    formatedProblem = str(num1) + op + str(num2)
    ansKey = eval(formatedProblem)

    # Get user answer
    ans = int(input(problem))
    questionCounter += 1

    # Check answer
    if ans == ansKey:
        correctCounter += 1

        print("Correct! {} seconds left!".format(int(
            60-(time.time() - startTime))))
    else:
        print("Incorrect! The correct answer is {}. {} seconds left!".format(ans, int(
            60-(time.time() - startTime))))

    percent = correctCounter / questionCounter * 100

print("You got {} out of {} questions correct! You percentage is {}.".format(
    correctCounter, questionCounter, percent))
