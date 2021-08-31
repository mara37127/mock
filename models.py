import peewee


class Transaction(peewee.Model):
    typeTransaction = peewee.CharField(index=True)

    amount = peewee.CharField()

    reference = peewee.CharField()

    clientNumber = peewee.CharField()

    date = peewee.CharField()

    time = peewee.CharField()

    state = peewee.CharField()

    simNumber = peewee.CharField()

    requestId = peewee.CharField()

    operator = peewee.CharField()

    modemIdentifier = peewee.CharField()
