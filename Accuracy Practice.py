import random
import simpy
import numpy as np

NUM_SURVIVORS = 5 #objects
ACCURACY = .03  #probability
SHOTS_PER_MINUTE = 25 #per minute
ZOMBIE_ATTACK_INTERVAL = 10 #per minute

SIM_TIME = 120 #minutes

zombies_killed = 0

class Apocalypse:

    def __init__(self, env, num_survivors, accuracy, shots_per_minute):
        self.env = env
        self.team = simpy.Resource(env, num_survivors)
        self.accuracy = accuracy
        self.shots_per_minute = shots_per_minute

    def defense(self, zombie):
        random_time = max(1, np.random.normal(self.shots_per_minute, 10))
        yield self.env.timeout(random_time)
        print(f"Dealt with {zombie} at {self.env.now:.2f}")

def zombie(env, survivors):
    global zombies_killed
    print(f"Zombie appears at {env.now:.2f}!")
    with survivors.team.request() as request:
        yield request
        print(f"Zombie engaged at {env.now:.2f}!")
        yield env.process(survivors.support)
        print(f"Zombie killed at {env.now:.2f}!")
        zombies_killed += 1

def setup(env, num_survivors, shots_per_minute, accuracy, zombie_attack_interval):
    survivors = Apocalypse(env, num_survivors, shots_per_minute, accuracy, zombie_attack_interval)

    for i in range(1, 6):
        env.process(zombie(env, i, survivors))
    
    while True:
        yield env.timeout(random.randint(zombie_attack_interval -1, zombie_attack_interval +1 ))
        i += 1
        env.process(zombie(env, num_survivors, survivors))

print("Starting Apocalypse")
env = simpy.Environment()
env.process(setup(env, NUM_SURVIVORS, ACCURACY, SHOTS_PER_MINUTE, ZOMBIE_ATTACK_INTERVAL))
env.run(until=SIM_TIME)

print("Zombies Killed: "  + str(zombies_killed))





