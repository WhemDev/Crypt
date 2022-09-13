from orm import Model
from orm import Database


class Person(Model):
    discord_id = int

    alert_symbol = str
    alert_symbol1 = str
    alert_symbol2 = str

    alert_price = float
    alert_price1 = float
    alert_price2 = float

    def __init__(self, discord_id, alert_symbol, alert_price):
        self.discord_id = discord_id
        self.alert_symbol = alert_symbol
        self.alert_price = alert_price

        #self.alert_symbol1 = alert_symbol
        #self.alert_price1 = alert_price

        #self.alert_symbol2 = alert_symbol
        #self.alert_price2 = alert_price


def get_user_or_false(discord_id):
    objects = Person.manager(db)
    users = list(objects.all())

    for user in users:
        if user.id == discord_id:
            return True

    return False


db = Database('alert.sqlite')
Person.db = db

