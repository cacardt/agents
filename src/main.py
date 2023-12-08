from agent import *
import random
import time

if __name__ == '__main__':
    agent1 = Agent("exemple", "exempleEquipe", 10, 2, 2, 6)
    agent2 = Agent("exemple2", "exempleEquipe", 10, 4, 2, 4)
    # create 10 agents with random stats each whose sum equals 20
    life = 0
    strength = 0
    speed = 0
    armor = 0
    agents = []
    for i in range(10):
        while(life + strength + speed + armor != 20):
            life = random.randint(1, 10)
            strength = random.randint(1, 10)
            speed = random.randint(1, 10)
            armor = random.randint(1, 10)
        agents.append(Agent(str(i), "exempleEquipe", life, strength, speed, armor))
    agents.append(agent1)
    agents.append(agent2)   

# for loop for every agent

while agents[0].isAlive() or agents[1].isAlive() or agents[2].isAlive() or agents[3].isAlive() or agents[4].isAlive() or agents[5].isAlive() or agents[6].isAlive() or agents[7].isAlive() or agents[8].isAlive() or agents[9].isAlive() or agents[10].isAlive() or agents[11].isAlive():
    for i in range(len(agents)):
        if agents[i].isAlive():
            obs = agents[i].observe()
            agents[i].act(obs)