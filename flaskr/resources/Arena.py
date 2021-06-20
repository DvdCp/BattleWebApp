from flaskr.challangers.Challenger import Challenger
from flaskr.challangers.Hero import Hero
from flaskr.challangers.Monster import Monster
from flaskr.challangers.lobbyparser.LobbyParser import LobbyParser
from flask import request, render_template, make_response
from flask_restful import Resource
from random import randint
from flaskr import app
from flaskr import battleLogger
import flaskr.utils.DatabaseHelper as DBHelper


class Arena(Resource):

    print("-----> INIZIALIZZAZIONE DELL'ARENA")
    # battleLogger = BattleLogger()

    def get(self):
        return make_response(render_template("index.html").encode())

    # ----- REDIRECT METHODS ----- #

    @staticmethod
    @app.route("/Arena/fight", methods=["POST"])
    def fight():
        # qua effettua la battaglia e restituisce i risultati
        lobbyRecieved = request.data
        lobby = LobbyParser.parseJSONtoLobby(lobbyRecieved)

        return Arena.startBattle(lobby)

    @staticmethod
    @app.route("/Arena/results")
    def results():
        # Recupero delle battaglie da DB
        results = DBHelper.Battle.query.all()

        return make_response(render_template('results.html', results=results)), 200

    @staticmethod
    @app.route("/Arena/createLobby")
    def create_lobby():
        return make_response(render_template('createlobby.html'))

    @staticmethod
    @app.route("/Arena/createChallanger")
    def create_challanger():
        return make_response(render_template('createchallanger.html'))

    # ----- BUSINESS METHODS ----- #
    @classmethod
    def startBattle(cls, challangerLobby: tuple[list[Hero], list[Monster]]):
        # Questo metodo fa partire una battaglia tra eroi e mostri.

        # Reset del BattleLog
        battleLogger.clearBattleLog()

        # Ottenimento dei membri della tupla
        _heroes, _monsters = challangerLobby

        while True:
            # TURNO DEGLI EROI: finchè c'è almeno un eroe e mostro vivi...
            if cls.checkIfSquadIsAlive(_heroes) and cls.checkIfSquadIsAlive(_monsters):
                # Seleziona un eroe a caso che attaccherà un mostro a caso
                randomHero = cls.getRandomHero(_heroes)
                randomMonster = cls.getRandomMonster(_monsters)
                randomHero.attack(randomMonster)

            # TURNO DEI MOSTRI: finchè c'è almeno un eroe e mostro vivi...
            if cls.checkIfSquadIsAlive(_heroes) and cls.checkIfSquadIsAlive(_monsters):
                # Seleziona un mostro a caso che attaccherà un eroe a caso
                randomHero = cls.getRandomHero(_heroes)
                randomMonster = cls.getRandomMonster(_monsters)
                randomMonster.attack(randomHero)

            if not cls.checkIfSquadIsAlive(_heroes):
                # Se a fine turno non ci sono eroi vivi, hanno vinto i mostri
                outcome = "La battaglia è conclusa.\n------------------------ HANNO VINTO I MOSTRI !!! ------------------------"
                battleLogger.recordEvent(outcome)
                DBHelper.Battle.insertBattle(battleLogger.getBattleLog())

                return battleLogger.getBattleLog()

            elif not cls.checkIfSquadIsAlive(_monsters):
                # Se a fine turno non ci sono mostri vivi, hanno vinto gli eroi
                outcome = "La battaglia è conclusa.\n------------------------ HANNO VINTO GLI EROI !!! ------------------------"
                battleLogger.recordEvent(outcome)
                DBHelper.Battle.insertBattle(battleLogger.getBattleLog())

                return battleLogger.getBattleLog()

    def getRandomHero(heroes: list[Hero]) -> Hero:
        # Questo metodo serve per recuperare un eroe vivo casuale dalla lista degli eroi
        while True:
            randomHeroIndex = randint(0, len(heroes) - 1)
            aHero = heroes[randomHeroIndex]
            if aHero.isAlive():
                return aHero

    def getRandomMonster(monsters: list[Monster]) -> Monster:
        # Questo metodo serve per recuperare un mostro vivo casuale dalla lista dei mostri
        while True:
            randomMonsterIndex = randint(0, len(monsters) - 1)
            aMonster = monsters[randomMonsterIndex]
            if aMonster.isAlive():
                return aMonster

    def checkIfSquadIsAlive(squad: list[Challenger]) -> bool:
        # Questo metodo serve per verificare se una data squadra ha ancora almeno un membro vivo
        for _challanger in squad:
            if _challanger.isAlive():
                return True
        return False
