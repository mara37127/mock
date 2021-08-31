from fastapi import Depends, FastAPI, HTTPException
from schemas import TransactionDTO, WizallFee
from models import Transaction as Tmodel
import requests
import json
import intouch.routes as routes



app = FastAPI(
    title="Mock KalpaY",
    version="1.0"
)
app.include_router(routes.router)

URL = "http://localhost:8081/transactions"
Transactions = []


@app.get('/transactions')
def getTransactions():
    return Transactions


@app.post('/validatedTransactions')
def validate(transactionDto: TransactionDTO):
    print("transactionDTO => ", transactionDto)
    Transactions.insert(len(Transactions), transactionDto)
    return 'Got it !'



@app.get('/test')
def getTest():
    return 'hello world'



