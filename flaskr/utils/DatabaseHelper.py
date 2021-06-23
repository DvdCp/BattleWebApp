from flaskr import app
from flask_sqlalchemy import SQLAlchemy
import os.path
import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utils/database.db'
db = SQLAlchemy(app)


def createDb():
    if os.path.isfile("../Esercizio5/utils/database.db"):
        print("------->Database già esistente")
    else:
        db.create_all()
        print("------->Nuovo Database creato")


# ----- TABLES ----- #

class Battle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    battle_events = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.String, nullable=False)

    def insertBattle(battleEvents: str) -> None:
        creation_date = str(datetime.datetime.now())
        battle = Battle(battle_events=battleEvents, creation_date=creation_date[:-7])
        db.session.add(battle)
        db.session.commit()

    def __repr__(self):
        return '<Battle: %r>' % self.battle_events