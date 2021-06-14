from random import randint
from Esercizio5.challangers.Challenger import Challenger


class Monster(Challenger):

    def __init__(self, name: str, race: str, lifePoints: float, damageAttack: float, dodgePercentage: int,
                 berserkTriggerPercentage: int) -> None:
        super().__init__(name, race, lifePoints, damageAttack, dodgePercentage)
        self.__berserkTriggerPercentage = berserkTriggerPercentage
        self.__onBerserk = False

    def attack(self, opponent) -> str:
            # Normal Attack
            return opponent.takeDamage(self.get__damageAttack())

    def takeDamage(self, damageToTake: float) -> str:
        dodgeAttempt = randint(0, 100)

        if dodgeAttempt < self.get__dodgePercentage():
            self.get__battleLogger().recordEvent(self.get__name() + " ha schivato l'attacco !")
        elif self.__onBerserk:
            self.get__battleLogger().recordEvent(self.get__name() + " riceve un colpo ma è una furia!!!")
            self.set__lifePoints(self.get__lifePoints() - (damageToTake - 10))
        else:
            self.get__battleLogger().recordEvent(self.get__name() + " ha subito un colpo!!!")
            self.set__lifePoints(self.get__lifePoints() - damageToTake)

            if not self.__onBerserk:
                berserkAttempt = randint(0, 100)
                if(berserkAttempt <= self.__berserkTriggerPercentage):
                    self.__onBerserk = True
                    self.get__battleLogger().recordEvent(self.get__name() + " E' IN BERSERK !!! DANNI RIDOTTI DI -10")

            if self.get__lifePoints() <= 0.00:
                self.die()

    def die(self) -> str:
        self.get__battleLogger().recordEvent(self.get__name() + " muore !")
        self.set__isAlive(False)
