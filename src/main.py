from agent import *
import time

if __name__ == '__main__':
    agent1 = Agent("exemple", "exempleEquipe", 10, 7, 7, 6)
    agent2 = Agent("exemple2", "exempleEquipe", 10, 7, 7, 6)

    while agent1.isAlive() or agent2.isAlive():

        if agent1.isAlive():
            obs = agent1.observe()
            agent1.act(obs)

        if agent2.isAlive():
            obs = agent2.observe()
            agent2.act(obs)