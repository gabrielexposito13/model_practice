import random
import simpy
import numpy as np

NUM_EMPLOYEES = 5 #objects
AVG_SUPPORT_TIME = 3 #minutes
CUSTOMER_INTERVAL = 4 #minutes
SIM_TIME = 120 #minutes

customers_handled = 0

class CallCenter:

    def __init__(self, env, num_employees, support_time):
        self.env = env
        self.num_employees = simpy.Resource(env, num_employees)
        self.support_time = support_time

    def support(self, customer):
        random_time = max(1, np.random.normal(self.support_time, 4))
        yield self.env.timeout(random_time)
        print(f"Support finished for {customer} at {self.env.now:.2f}")

def customer(env, name, call_center):
    global customers_handled
    print(f"Customer {name} enters waiting queue at {env.now:.2f}!")


        