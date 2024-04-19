import gymnasium as gym
import numpy

env = gym.make("ALE/Frogger-v5", render_mode="human")
#render_module: human, rgb_array, ansi, rgb_array_list, ansi_list 

observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()  # agent policy that uses the observation and info
                                        # akcja tutaj moze byc liczba 0-4
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()