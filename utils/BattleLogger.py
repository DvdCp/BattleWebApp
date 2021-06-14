class BattleLogger:

    def __init__(self):
        self.__battleLog = str()
        self.__serverLog = str()

    def recordEvent(self, outcomeToRecord: str) -> str:
        self.__battleLog += outcomeToRecord + "\n"

    def recordLastBattle(self) -> str:
        self.__serverLog += self.__battleLog + "\n"

    def clearBattleLog(self):
        self.__battleLog = ""

    def getBattleLog(self) -> str:
        return self.__battleLog

    def getServerLog(self) -> str:
        return self.__serverLog