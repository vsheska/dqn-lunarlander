import gymnasium as gym

env = gym.make("LunarLander-v3")
obs, _ = env.reset()
print("Initial observation:", obs)