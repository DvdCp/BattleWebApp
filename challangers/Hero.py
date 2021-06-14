from random import randint
from Esercizio5.challangers.Challenger import Challenger


class Hero(Challenger):

    def __init__(self, name: str, race: str, lifePoints: float, damageAttack: float, dodgePercentage: int,
                 heroClass: str, focusTriggerPercentage: int) -> None:
        super().__init__(name, race, lifePoints, damageAttack, dodgePercentage)
        self.__heroClass = heroClass
        self.__focusTriggerPercentage = focusTriggerPercentage
        self.__onFocus = False

    def attack(self, opponent) -> None:

        opponent.takeDamage(self.get__damageAttack())

        if self.__onFocus:
            self.get__battleLogger().recordEvent(self.get__name() + " scaglia un'altro colpo con agilità !")
            opponent.takeDamage((self.get__dodgePercentage() / 3))

        if not self.__onFocus:
            focusAttempt = randint(0, 100)
            if focusAttempt <= self.__focusTriggerPercentage:
                self.__onFocus = True
                self.get__battleLogger().recordEvent(self.get__name() + " è preso dalla battaglia !!! Per ogni attacco effettua un contraccolpo")

    def takeDamage(self, damageToTake: float) -> None:

        dodgeAttempt = randint(0, 100)

        if dodgeAttempt < self.get__dodgePercentage():
            self.get__battleLogger().recordEvent(self.get__name() + " schiva il colpo!")
            pass  # no damage taken

        else:  # take damage
            self.get__battleLogger().recordEvent(self.get__name() +  " è stato colpito dal mostro!")
            self.set__lifePoints(self.get__lifePoints() - damageToTake)

            if self.get__lifePoints() <= 0.00:
                self.die()

    def die(self) -> None:
        self.get__battleLogger().recordEvent(self.get__name() + " è stato sconfitto!")
        self.set__isAlive(False)
