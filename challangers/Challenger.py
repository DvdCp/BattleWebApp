import abc
from Esercizio5 import battleLogger


class Challenger(metaclass=abc.ABCMeta):

    def __init__(self, name: str, race: str, lifePoints: float, damageAttack: float, dodgePercentage: float) -> None:
        self.__name = name
        self.__race = race
        self.__lifePoints = lifePoints
        self.__maxLifePoints = lifePoints
        self.__damageAttack = damageAttack
        self.__dodgePercentage = dodgePercentage
        self.__isAlive = True
        self.__battleLogger = battleLogger

    def __repr__(self):
        return str(self.__dict__)

    @abc.abstractmethod
    def attack(self, opponent) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def takeDamage(self, damageToTake: float) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def die(self) -> None:
        raise NotImplementedError

    # Questo dunder method serve per controllare se la classe di un determinato oggetto è sottoclasse di Challanger.
    # Tale controllo viene eseguito verificando "manualmente" se il nome degli attributi e metodi presenti nella
    # sottoclasse e superclasse coincidono.
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "__name") and
                hasattr(subclass, "__race") and
                hasattr(subclass, "__lifePoints") and
                hasattr(subclass, "__damageAttack") and
                hasattr(subclass, "__dodgePercentage") and
                hasattr(subclass, "attack") and
                callable(subclass.attack) and
                hasattr(subclass, "takeDamage") and
                callable(subclass.takeDamage) and
                hasattr(subclass, "die") and
                callable(subclass.die) or
                NotImplemented)

    def resetLifePoints(self):
        self.__lifePoints = self.__maxLifePoints

    # -/*/*/*/*/*/*/*\ GETTERS & SETTER /*\*\*\*\*\*\*\-
    def get__name(self) -> str:
        return self.__name

    def get__race(self) -> str:
        return self.__race

    def get__lifePoints(self) -> str:
        return self.__lifePoints

    def set__lifePoints(self, value) -> float:
        self.__lifePoints = value

    def get__damageAttack(self) -> float:
        return self.__damageAttack

    def get__dodgePercentage(self) -> float:
        return self.__dodgePercentage

    def isAlive(self) -> bool:
        return self.__isAlive

    def set__isAlive(self, value: bool):
        self.__isAlive = value

    def get__battleLogger(self):
         return self.__battleLogger