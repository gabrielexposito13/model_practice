import random
import simpy
import numpy as np

DEER = 40
DISTANCE = 100
EVASION_CHANCE = 0.85
HIT_CHANCE = 0.60
SIM_TIME = 100

deer_hunted = 0

class Hunter:
    def __innit__(self, env, deer, evasion_chance):
        self.env = env
        self.horde = simpy.Resource(env, deer)
        self.evasion_chance = evasion_chance

    def attack(self, env, survivor, hit_chance):
        random_time = max(1, np.random.normal(self.evasion_chance, 0.60))
        yield self.env.timeout(random_time)
        self.env = env
        self.sam = simpy.Resource(env, survivor)
        self.hit_chance = hit_chance
    
def scenario(env, engagement):
    global deer_killed
    print(f"deer enters the zone.")
    with engagement.squadron() as request:
        yield request
        print(f"deer enters danger zone.")
        yield env.process(engagement.attack)
        print(f"deer has been hit")
        blue_downed += 1

def setup(env, blue, evasion_chance, hit_chance):
    engagement = Hunter(env, blue, evasion_chance, hit_chance)

    for i in range(1 , 5):
        env.process(engagement(env, i, engagement))

        while True:
            yield env.timeout(random.randint(hit_chance -1, hit_chance +1))
            i += 1
            env.process(engagement(env, blue, engagement))

print("Starting Simulation")
env = simpy.Environment()
env.process(setup(env, deer, EVASION_CHANCE, HIT_CHANCE))
env.run(until1=SIM_TIME)

print("Deer Hunted: " +str(deer_hunted))




