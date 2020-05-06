
import random
count = 0


def roller():
    global count
    count += 1
    num_choice = range(1, 7)
    num = num_choice[random.randint(1, 6)]
    print("The dice landed on " + "{}\n".format(num))
    choice = input("Do you want to roll again(y/n): ")
    choice = choice.strip()
    if choice == "y" and count < 20:
        roller()
    else:
        pass


roller()

"""
import random
count = 0


def roller():
    global count
    count += 1
    num_choice = range(1, 7)
    num = num_choice[random.randint(1, 6)]
    print("The dice landed on " + "{}\n".format(num))


def attempts(rolller):
    choice = input("Do you want to roll again(y/n): ")
    if choice == "y":
        roller()
        attempts(roller)
    else:
        pass


attempts(roller())

"""

