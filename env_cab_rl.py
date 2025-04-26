# env_cab_rl.py
import gym
import random

class CabEnv(gym.Env):
    def __init__(self):
        super(CabEnv, self).__init__()
        self.action_space = gym.spaces.Discrete(4)  # 0: idle, 1: short ride, 2: medium ride, 3: long ride
        self.observation_space = gym.spaces.Discrete(20)  # 20 different time-locations (state IDs)
        self.state = 0

    def reset(self):
        self.state = random.randint(0, 19)
        return self.state

    def step(self, action):
        reward = 0
        done = False

        if action == 0:
            reward = -1  # idle penalty
        elif action == 1:
            reward = random.randint(5, 10)
        elif action == 2:
            reward = random.randint(10, 20)
        elif action == 3:
            reward = random.randint(20, 30)

        self.state = random.randint(0, 19)
        return self.state, reward, done, {}
