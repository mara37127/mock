
from typing import Optional

from pydantic import BaseModel


class Transaction(BaseModel):
    typeTransaction: Optional[str] = None

    amount: Optional[str] = None

    reference: Optional[str] = None

    clientNumber: Optional[str] = None

    date: Optional[str] = None

    time: Optional[str] = None

    state: Optional[str] = None

    simNumber: Optional[str] = None

    requestId: Optional[str] = None

    operator: Optional[str] = None

    modemIdentifier: Optional[str] = None

    class Config:
        orm_mode = True


class TransactionDTO(BaseModel):

    typeTransaction: Optional[str] = None

    amount: Optional[str] = None

    clientNumber: Optional[str] = None

    date: Optional[str] = None

    time: Optional[str] = None

    state: Optional[str] = None

    requestId: Optional[str] = None

    operator: Optional[str] = None

    class Config:
        orm_mode = True


class Transaction(BaseModel):
    typeTransaction: Optional[str] = None

    amount: Optional[str] = None

    reference: Optional[str] = None

    clientNumber: Optional[str] = None

    date: Optional[str] = None

    time: Optional[str] = None

    state: Optional[str] = None

    simNumber: Optional[str] = None

    requestId: Optional[str] = None

    operator: Optional[str] = None

    modemIdentifier: Optional[str] = None

    class Config:
        orm_mode = True


class IntouchModel(BaseModel):

    service_id: Optional[str] = None

    recipient_phone_number: Optional[str] = None

    amount: Optional[str] = None

    partner_id: Optional[str] = None

    partner_transaction_id: Optional[str] = None

    login_api: Optional[str] = None

    password_api: Optional[str] = None

    call_back_url: Optional[str] = None

    frais: Optional[str] = None


    class Config:
        orm_mode = True


class WizallFee(BaseModel):

    service_id: Optional[str] = None

    recipient_phone_number: Optional[str] = None

    amount: Optional[str] = None

    partner_id: Optional[str] = None

    login_api: Optional[str] = None

    password_api: Optional[str] = None

    typeOperation: Optional[str] = None

    frais: Optional[str] = None

    class Config:
        orm_mode = True


class Balance(BaseModel):

    partner_id: Optional[str] = None

    login_api: Optional[str] = None

    password_api: Optional[str] = None

    class Config:
        orm_mode = True


class Status(BaseModel):

    partner_id: Optional[str] = None

    login_api: Optional[str] = None

    password_api: Optional[str] = None

    partner_transaction_id: Optional[str] = None

    class Config:
        orm_mode = True


class Yup(BaseModel):

    serviceId: Optional[str] = None

    clientNumber: Optional[str] = None

    amount: Optional[str] = None

    partnerId: Optional[str] = None

    partnerTransactionId: Optional[str] = None

    loginApi: Optional[str] = None

    passwordApi: Optional[str] = None

    type: Optional[str] = None

    currency: Optional[str] = None

    compte: Optional[str] = None


    class Config:
        orm_mode = True


class YupGetStatus(BaseModel):


    clientNumber: Optional[str] = None

    amount: Optional[str] = None

    partnerId: Optional[str] = None

    loginApi: Optional[str] = None

    passwordApi: Optional[str] = None

    type: Optional[str] = None

    currency: Optional[str] = None

    compte: Optional[str] = None


    class Config:
        orm_mode = True