from flask import Flask
from flaskr.utils.BattleLogger import BattleLogger

battleLogger = BattleLogger()
app = Flask(__name__)