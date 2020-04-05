import gym 
import gym_snake

env = gym.make('snake-v0')
env.reset()
for _ in range(10):
    env.render()
    snake, food, score, done = env.step(env.action_space.sample()) # take a random action
    print( "Snake: {}\nFood: {}\nScore: {}\nDone: {}".format(snake, food, score, done))
env.close()

# import gym
# env = gym.make('CartPole-v0')
# env.reset()
# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample()) # take a random action
# env.close()