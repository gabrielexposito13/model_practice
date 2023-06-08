import random

# Define the constants

TIM_ACCURACY_AT_30_METERS = 100
TIM_ACCURACY_DECREASE_PER_METER_ABOVE_30 = 3
TIM_ACCURACY_DECREASE_PER_METER_BELOW_25 = 5
ROB_CLOSEST_APPROACH_TO_TIM = 15
ROB_SPEED = 2
TIM_BOTTLES = 12
TIM_BOTTLES_USED_AT_60_METERS_OR_FARTHER = 0.4 * TIM_BOTTLES
TIM_BOTTLES_USED_BETWEEN_59_AND_31_METERS = 0.3 * TIM_BOTTLES

# Initialize the variables

tim_accuracy = TIM_ACCURACY_AT_30_METERS
tim_bottles_left = TIM_BOTTLES
rob_distance_from_tim = ROB_CLOSEST_APPROACH_TO_TIM
rob_shield_hits = 0

# Start the simulation

while rob_distance_from_tim > 0:

    # Calculate the number of bottles that Tim will throw

    if rob_distance_from_tim >= 60:
        bottles_thrown = TIM_BOTTLES_USED_AT_60_METERS_OR_FARTHER
    elif rob_distance_from_tim < 31:
        bottles_thrown = TIM_BOTTLES_USED_BETWEEN_59_AND_31_METERS
    else:
        bottles_thrown = tim_bottles_left

    # Calculate the probability of Tim hitting Rob

    probability_of_hit = tim_accuracy * (1 - (rob_distance_from_tim - 30) * TIM_ACCURACY_DECREASE_PER_METER_ABOVE_30) * (1 - (30 - rob_distance_from_tim) * TIM_ACCURACY_DECREASE_PER_METER_BELOW_25)

    # Throw the bottles

    for bottle in range(bottles_thrown):

        # Check if Rob is hit

        hit = random.randint(0, 100) < probability_of_hit

        # If Rob is hit, update the shield hits and bottles left

        if hit:
            rob_shield_hits += 1
            tim_bottles_left -= 1

    # Update the distance between Rob and Tim

    rob_distance_from_tim -= rob_speed

# Check if Rob was hit

if rob_shield_hits < 5:
    print("Rob was hit")
else:
    print("Rob was not hit")
