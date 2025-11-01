# Elevator exercise
class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current = bottom

    def go_to_floor(self, floor):
        if floor > self.current:
            for i in range(floor - self.current):
                self.floor_up()
        elif floor < self.current:
            for i in range(self.current - floor):
                self.floor_down()
        print(f"Now at floor {self.current}")

    def floor_up(self):
        if self.current < self.top_floor:
            self.current += 1
            print(f"Going up... floor {self.current}")

    def floor_down(self):
        if self.current > self.bottom_floor:
            self.current -= 1
            print(f"Going down... floor {self.current}")


# Building class
class Building:
    def __init__(self, bottom, top, elevators_count):
        self.elevators_list = []
        for i in range(elevators_count):
            self.elevators_list.append(Elevator(bottom, top))

    def run_elevator(self, elevator_num, destination):
        print(f"Using elevator {elevator_num}")
        self.elevators_list[elevator_num].go_to_floor(destination)

    def fire_alarm(self):
        print("FIRE ALARM! Going to ground floor!")
        for elev in self.elevators_list:
            elev.go_to_floor(elev.bottom_floor)


# Testing
if __name__ == "__main__":
    print("Testing elevator:")
    test_elevator = Elevator(1, 10)
    test_elevator.go_to_floor(5)
    test_elevator.go_to_floor(1)

    print("\nTesting building:")
    my_building = Building(1, 15, 3)
    my_building.run_elevator(0, 7)
    my_building.run_elevator(1, 10)
    my_building.fire_alarm()