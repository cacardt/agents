import requests

class Agent:
    def __init__(self, cid, teamid, life, strength, speed, armor):
        self.cid = cid
        self.teamid = teamid
        self.life = life
        self.strength = strength
        self.speed = speed
        self.armor = armor

    def call_api(url, headers=None, params=None):
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data

    def act(self, observation):

        # sélectionne et exécute une action en fonction de l'observation, qui est l'état de l'arène.
        # il faut ici faire appel aux routes de l'API !
        pass

    def observe(self):
        # récupère l'état de l'arène et le retourne
        return 0

    def isAlive(self):
        # retourne vrai si life > 0, false sinon
        alive = False
        if(self.life > 0):
            alive = True
        return alive