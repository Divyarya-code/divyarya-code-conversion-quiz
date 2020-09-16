import time

#getting_inputs
hour = int(input("Type the current hour:"))
minute = int(input("Type the current minute:"))
second = int(input("Type the current second:"))

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


