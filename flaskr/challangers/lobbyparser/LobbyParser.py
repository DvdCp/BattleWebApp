import json
from flaskr.challangers.Hero import Hero
from flaskr.challangers.Monster import Monster


class LobbyParser:

    @staticmethod
    def parseJSONtoLobby(jsonLobby) -> tuple[list[Hero], list[Monster]]:
        lobbyAsList = json.loads(jsonLobby)
        _heroesAsDicts = lobbyAsList[0]
        _monstersAsDicts = lobbyAsList[1]
        _heroes = list()        #Lista di eroi che comporrà la lobby
        _monsters = list()      #Lista di mostri che comporrà la lobby

        for _heroDict in _heroesAsDicts.get("Heroes"):
        # Per ogni dict che descrive un eroe, crea un oggetto Hero usando i valori del dict
            _heroes.append(Hero(**_heroDict))
        for _monsterDict in _monstersAsDicts.get("Monsters"):
        # Per ogni dict che descrive un mostro, crea un oggetto Monster usando i valori del dict
            _monsters.append(Monster(**_monsterDict))

        return _heroes, _monsters