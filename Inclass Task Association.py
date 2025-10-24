class Pupil:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def attendance(self, times):
        for i in range(times):
            print(self.name + " is present.")


class Instructor:
    def __init__(self):
        self.pupils = []

    def mark_present(self, pupil):
        self.pupils.append(pupil)
        print(pupil.name + " is marked present.")

    def mark_absent(self, pupil):
        if pupil in self.pupils:
            self.pupils.remove(pupil)
            print(pupil.name + " is marked absent.")
        else:
            print(pupil.name + " was not marked present earlier.")

    def greet_pupils(self):
        for pupil in self.pupils:
            print(pupil.name + " says: Hello!!")


# Creating pupil objects
pupil1 = Pupil("Mili", roll_no=1)
pupil2 = Pupil("Maxy", roll_no=8)
pupil3 = Pupil("Kelvin", roll_no=5)
pupil4 = Pupil("Jimmy", roll_no=2)
pupil5 = Pupil("Jacky", roll_no=9)

# Creating instructor object
instructor = Instructor()

# Marking attendance and greeting
instructor.mark_present(pupil1)
instructor.mark_present(pupil2)
instructor.mark_present(pupil3)
instructor.greet_pupils()

instructor.mark_present(pupil4)
instructor.mark_present(pupil5)
instructor.greet_pupils()
