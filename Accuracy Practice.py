import random

class Tim:

    def __init__(self, accuracy_max, accuracy_decrease_per_meter_100_to_30, accuracy_decrease_per_meter_25_to_0, closest_approach_to_rob, bottles_in_box):
        self.accuracy_max = accuracy_max
        self.accuracy_decrease_per_meter_100_to_30 = accuracy_decrease_per_meter_100_to_30
        self.accuracy_decrease_per_meter_25_to_0 = accuracy_decrease_per_meter_25_to_0
        self.closest_approach_to_rob = closest_approach_to_rob
        self.bottles_in_box = bottles_in_box
        self.bottles_used = 0

    def throw_bottles(self, rob_distance):

        # Calculate Tim's accuracy
        if rob_distance >= 60:
            self.accuracy = self.accuracy_max - (rob_distance - 60) * self.accuracy_decrease_per_meter_100_to_30
        elif rob_distance < 30:
            self.accuracy = self.accuracy_max - (30 - rob_distance) * self.accuracy_decrease_per_meter_25_to_0
        else:
            self.accuracy = self.accuracy_max

        # Calculate the number of bottles Tim will throw
        number_of_bottles_to_throw = random.randint(0, self.bottles_in_box)
        number_of_bottles_to_throw = min(number_of_bottles_to_throw, self.bottles_in_box * (40 / 100) if rob_distance >= 60 else self.bottles_in_box * (30 / 100) if rob_distance <= 31 else self.bottles_in_box)

        # Throw the bottles
        for i in range(int(number_of_bottles_to_throw)):
            if random.random() <= self.accuracy / 100:
                print("Tim hit Rob!")
            else:
                print("Tim missed Rob!")

        # Update Rob's distance from Tim
        rob_distance += 2

        # Update the number of bottles Tim has used
        self.bottles_used += number_of_bottles_to_throw

class Rob:

    def __init__(self, closest_approach_to_tim, speed):
        self.closest_approach_to_tim = closest_approach_to_tim
        self.speed = speed
        self.distance_from_tim = closest_approach_to_tim

    def move(self):
        self.distance_from_tim += self.speed

def main():

    # Create a Tim object
    tim = Tim(100, 3, 5, 15, 12)

    # Create a Rob object
    rob = Rob(15, 2)

    # Run the simulation until Tim runs out of bottles
    while tim.bottles_used < tim.bottles_in_box:

        # Update Rob's position
        rob.move()

        # Tim throws bottles at Rob
        tim.throw_bottles(rob.distance_from_tim)

        # Print the number of bottles Tim used
        print("Tim used {} bottles.".format(tim.bottles_used))

if __name__ == "__main__":
    main()
