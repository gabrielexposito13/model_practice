import random

# Define constants
tim_accuracy_max = 100
tim_accuracy_decrease_per_meter_100_to_30 = 3
tim_accuracy_decrease_per_meter_25_to_0 = 5
tim_closest_approach_to_rob = 15
tim_bottles_in_box = 12
tim_bottles_used_at_60_meters_or_farther_percentage = 40
tim_bottles_used_at_59_to_31_meters_percentage = 30

# Initialize variables
tim_accuracy = tim_accuracy_max
tim_bottles_used = 0
rob_distance_from_tim = tim_closest_approach_to_rob

# While Rob is within Tim's range
while rob_distance_from_tim <= 100:

    # Calculate Tim's accuracy
    if rob_distance_from_tim >= 60:
        tim_accuracy = tim_accuracy_max - (rob_distance_from_tim - 60) * tim_accuracy_decrease_per_meter_100_to_30
    elif rob_distance_from_tim < 30:
        tim_accuracy = tim_accuracy_max - (30 - rob_distance_from_tim) * tim_accuracy_decrease_per_meter_25_to_0
    else:
        tim_accuracy = tim_accuracy_max

    # Calculate the number of bottles Tim will throw
    number_of_bottles_to_throw = random.randint(0, tim_bottles_in_box)

    # Throw the bottles
    for i in range(number_of_bottles_to_throw):
        if random.random() <= tim_accuracy / 100:
            print("Tim hit Rob!")
        else:
            print("Tim missed Rob!")

    # Update Rob's distance from Tim
    rob_distance_from_tim += 2

# Print the number of bottles Tim used
print("Tim used {} bottles.".format(tim_bottles_used))
