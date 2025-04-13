from helpers import *
import os

wkouts = []

def loadWorkouts():
    file = open("wkouts.txt", "r")

def saveWorkouts():
    file = open("wkouts.txt", "w")

def start():
    check = 1
    while (check == 1):
        option = input("Display workouts or create a new workout? (D/C) ")
        if option.lower() == "d":
            dispWorkouts()
        elif option.lower() == "c":
            createWorkout()

def dispWorkouts():
    x = 1
    for wkout in wkouts:
        wkout.display(x)
        print("\n")
        x += 1

def createWorkout():
    cont = 1
    name = input ("What would you like to call this workout? ")
    workout = Workout(name)
    index = 1

    while cont == 1:
        print(f"Excercise {index}")
        name = input("Name: ")
        weight = input("Weight: ")
        sets = input("Sets: ")
        reps = input("Reps: ")

        workout.addExcercise(Excercise(name, weight, sets, reps))
        index += 1

        if input("Would you like to add another excercise? (y/n) ").lower() == "y":
            cont = 1
        else:
            cont = 0

    wkouts.append(workout)

start()
