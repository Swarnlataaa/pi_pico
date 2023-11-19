import utime

def task1():
    while True:
        print("Task 1")
        utime.sleep(1)

def task2():
    while True:
        print("Task 2")
        utime.sleep(2)

# Run tasks in a cooperative manner
while True:
    task1()
    task2()
