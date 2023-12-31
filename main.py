import random
class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.15
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.progress += -0.1
        self.gladness += 3

    def is_alive(self):
        if self.progress < -0.5:
            print("Cant out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depreston...")
            self.alive = False
        elif self.progress > 5:
            print ("Passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness {self.gladness}")
        print(f"Progress = {self.progress}")
    def live(self, day):
        s = f"Day {day} of {self.name} life"
        print(f"{s:=^50}")
        live_cube = random.randint( 1,3)
        if live_cube == 1:
            self.to_chill()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_study()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nikolas")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
