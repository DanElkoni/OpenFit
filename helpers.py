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
        self.workouts = []

    def addExcercise(self, excercise):
        self.workouts.append(excercise)