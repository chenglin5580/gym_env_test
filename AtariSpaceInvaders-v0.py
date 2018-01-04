
import gym
from gym import envs
env_all = envs.registry.all()
print(env_all)
env = gym.make('SpaceInvaders-v0')
print(env.action_space)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)


for ep in range(100):
    observation = env.reset()
    for t in range(1000):
        env.render()
        # print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)  # take a random action
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break


