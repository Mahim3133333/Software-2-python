import random


# Car class from previous exercise
class Car:
    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours


# Race class
class Race:
    def __init__(self, name, km, cars):
        self.race_name = name
        self.distance_km = km
        self.cars_list = cars

    def hour_passes(self):
        for car in self.cars_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n--- {self.race_name} Status ---")
        print("Car Plate   | Speed | Distance")
        print("-----------------------------")
        for car in self.cars_list:
            print(f"{car.plate}    | {car.speed:3}   | {car.distance:6.1f} km")

    def race_finished(self):
        for car in self.cars_list:
            if car.distance >= self.distance_km:
                return True
        return False


# Main program
def main():
    # Create 10 cars
    cars = []
    for i in range(1, 11):
        max_spd = random.randint(120, 180)
        cars.append(Car(f"ABC-{i}", max_spd))

    # Create race
    demolition_derby = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    print("Race starting! 8000 km to go!")

    while not demolition_derby.race_finished():
        demolition_derby.hour_passes()
        hours += 1

        if hours % 10 == 0:
            demolition_derby.print_status()
            print(f"Hour: {hours}")

    # Final results
    print("\n*** RACE OVER! ***")
    demolition_derby.print_status()
    print(f"Total hours: {hours}")

    # Find winner
    winner = None
    for car in cars:
        if car.distance >= 8000:
            winner = car
            break

    if winner:
        print(f"Winner: {winner.plate}")
    else:
        # In case no one exactly reached 8000, find closest
        winner = max(cars, key=lambda x: x.distance)
        print(f"Best car: {winner.plate} with {winner.distance:.1f} km")


if __name__ == "__main__":
    main()