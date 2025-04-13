# Excercise class
class Excercise:
    def __init__(self, name, weight, sets, reps):
        self.name = name
        self.weight = weight
        self.sets = sets
        self.reps = reps
    
    def incrementWeight(self, amt):
        self.weight += amt

# Workout, list of excercises
class Workout:
    def __init__(self, name):
        self.name = name
        self.excercises = []

    def addExcercise(self, excercise):
        self.excercises.append(excercise)

    def display(self, num):
        print(f"Workout {num}: {self.name}")
        x = 1
        for excercise in self.excercises:
            print(f"Excercise {x}: {excercise.name} at {excercise.weight}lbs for {excercise.sets}x{excercise.reps} reps")
            x+=1
