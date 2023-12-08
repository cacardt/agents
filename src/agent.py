import requests
URL_API = "http://127.0.0.1:5000"
number = [1]


class Agent:
    def __init__(self, cid, teamid, life, strength, speed, armor):
        self.cid = cid
        self.teamid = teamid
        self.life = life
        self.strength = strength
        self.speed = speed
        self.armor = armor
    
    def call_api(self, url, method, data=None):
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, json=data)
        data = response.json()
        print("data", data)
        return data

    def act(self, observation):
        lowerLife = 20
        lowerPlayer = ""
        action = 0
        playersIn = observation[0]
        arenaState = observation[1]
        print("État de l'arène", arenaState)
        self.call_api(f"{URL_API}/character/join", "POST", {"cid": self.cid, "teamid": self.teamid, "life": self.life, "strength": self.strength, "speed": self.speed, "armor": self.armor})
        for i in range(len(playersIn)):
            if(playersIn[i]["cid"] != self.cid):
                if(playersIn[i]["life"] < lowerLife and self.life >= 5):
                    lowerLife = playersIn[i]["life"]
                    lowerPlayer = playersIn[i]["cid"]
                    action = 0
                elif(self.life < 5):
                    lowerPlayer = ""
                    action = 1
                else:
                    lowerPlayer = ""
                    action = 2
        self.call_api(f"{URL_API}/character/action", "POST", {"cid": self.cid, "target": lowerPlayer, "action": action})
        # sélectionne et exécute une action en fonction de l'observation, qui est l'état de l'arène.
        # il faut ici faire appel aux routes de l'API !

    def observe(self):
        observation = []
        observation.append(self.call_api(f"{URL_API}/characters", "GET"))
        observation.append(self.call_api(f"{URL_API}/arenaState", "GET"))

        # récupère l'état de l'arène et le retourne
        return observation

    def isAlive(self):
        # retourne vrai si life > 0, false sinon
        alive = False
        if(self.life > 0):
            alive = True
        return alive