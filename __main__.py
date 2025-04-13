from helpers import *
import os

wkouts = []

def createWorkout():
    cont = 1
    name = input ("What would you like to call this workout? ")
    wkouts.append(Workout(name))
    index = len(wkouts) - 1

    while cont == 1:
        print("Excercise []")
        name = input("Name: ")
        weight = input("Weight: ")
        sets = input("Sets: ")
        reps = input("Reps: ")

        wkouts[index].addExcercise(Excercise(name, weight, sets, reps))

        if input("Would you like to add anpther excercise? (y/n) ").lower() == "y":
            cont = 1
        else:
            cont = 0

createWorkout()