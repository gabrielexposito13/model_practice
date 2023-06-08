import numpy as np
import simpy
import random

ROB_CLOSEST_APPROACH_TO_TIM = 101

class Tim:
    def __init__(self, env):
        self.env = env
        self.bottles = 12
        self.accuracy_at_30_meters = 90
        self.accuracy_decrease_per_meter_above_30 = 5
        self.accuracy_decrease_per_meter_below_25 = 7
        self.closest_approach_to_tim = ROB_CLOSEST_APPROACH_TO_TIM
        self.speed = 2

    def throw_bottles(self, rob):
        # Calculate the number of bottles that Tim will throw
        if rob.distance_from_tim >= 60:
            bottles_thrown = int(0.4 * self.bottles)
        elif rob.distance_from_tim < 31:
            bottles_thrown = int(0.3 * self.bottles)
        else:
            bottles_thrown = int(self.bottles)

        # Calculate the probability of Tim hitting Rob
        probability_of_hit = self.accuracy_at_30_meters * (1 - (rob.distance_from_tim - 30) * self.accuracy_decrease_per_meter_above_30) * (1 - (30 - rob.distance_from_tim) * self.accuracy_decrease_per_meter_below_25)

        # Throw the bottles
        for bottle in range(bottles_thrown):

            # Check if Rob is hit
            hit = random.randint(0, 100) < probability_of_hit

            # If Rob is hit, update the shield hits and bottles left
            if hit:
                rob.shield_hits += 1
                self.bottles -= 1

        # Update the distance between Rob and Tim
        rob.distance_from_tim -= rob.speed


class Rob:
    def __init__(self, env):
        self.env = env
        self.shield_hits = 0
        self.distance_from_tim = ROB_CLOSEST_APPROACH_TO_TIM
        self.speed = 2

    def walk(self):
        while self.distance_from_tim > 0:
            self.distance_from_tim -= self.speed

    def pull_out_shield(self):
        self.shield_hits = 0


env = simpy.Environment()
tim = Tim(env)
rob = Rob(env)

for i in range(100):
    tim.throw_bottles(rob)
    rob.walk()

    if rob.shield_hits < 5:
        print("Rob was hit in simulation {}.".format(i + 1))
    else:
        print("Rob was not hit in simulation {}.".format(i + 1))
