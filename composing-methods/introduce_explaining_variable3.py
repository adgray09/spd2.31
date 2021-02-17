# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class Cooking:
    def __init__(self, time, temperature, pressure, desired_state):
        self.time = time
        self.temperature = temperature
        self.pressure = pressure
        self.desired_state = desired_state
        
    def is_criteria_satisfied(self):
        return self.is_medium() or self.is_well_done()
    
    def is_well_done(self):
        return self.desired_state == "well-done" and self.cooking_progress() >= WELL_DONE
    
    def cooking_progress(self):
        return self.time * self.temperature * self.pressure * COOKED_CONSTANT
    
    def is_medium(self):
        return self.desired_state == "medium" and self.cooking_progress() >= MEDIUM
    
    def is_done_cooking(self):
        if self.is_criteria_satisfied():
            print('cooking is done')
        else:
            print('keep cooking')
    
    
alex_steak = Cooking(30, 100, 20, "well-done")

alex_steak.is_done_cooking()