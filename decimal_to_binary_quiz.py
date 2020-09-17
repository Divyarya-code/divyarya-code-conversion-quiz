import time
import random
random_num = random.randint(0,100)
print("Welcome CHAMP, ready for quiz! \n Rules of quiz are: \n 1.We give you a random number between 1 to 100 \n 2.You have to convert it into Binary number in 60 seconds \n 3.After 60 second you have to write your answer, you have only one attempt \n best of luck :)")
print("Convert this number into binary number:", random_num)

#decimal_to_binary
def decimal_to_binary(n):
    bits = []

    while n>0:
        bits.append(n%2)
        n = n//2
        bits.reverse()

    binary = ''
    for element in bits:
        binary = binary + str(element)
    return binary

num = random_num

#getting_inputs
print("your clock time is auto set at 1 second")
hour = int(input("Type the current hour:"))
minute = int(input("Type the current minute:"))
second = 1

#function_for_displaying_time
def display():
    print(hour,':',minute,':',second)

#function_for_increament
def add():
    global hour
    global minute
    global second

    second = second+1
    if second == 60:
        minute = minute+1
        second = 0

    if minute == 60:
        hour = hour+1
        minute = 0

    if hour == 24:
        hour = 0


print("\n")

#infinite_loop
while True:
    time.sleep(1)
    add()
    display()

    if second == 0:
        response = input("enter your answer:")
        if response == decimal_to_binary(num):
            print("congratulation your answer is right")
            break
        else:
            print("sorry your answer is wrong, correct answer is:", decimal_to_binary(num))
            break


