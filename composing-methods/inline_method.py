# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 18
class Person:
    def __init__(self, my_age):
        self.age = my_age
        
    def enter_night_club(self):
        if self.age > LEGAL_DRINKING_AGE:
            print("Allowed to enter.")
        else:
            print("Enterance of minors is denied.")
    
    
person = Person(17.9)
person2 = Person(20)            

person.enter_night_club()
person2.enter_night_club()
        
