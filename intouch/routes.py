from fastapi import APIRouter, Request
import schemas



router = APIRouter(
    prefix='/intouch',
    tags=['intouch'],
    responses={404: {"description": "Not found"},
               400: {"description": "Bad request"},
               401: {"description": "Unauthorized"}, }
)

callbacks = []


@router.post("/cashin")
async def cashin(data: schemas.IntouchModel):
    """
    Cashin
    """
    print(data)
    return data

@router.post("/get_frais")
def getFrais(data: schemas.WizallFee):
    print(data)
    return '15'


@router.post("/get_balance")
def getFrais(data: schemas.Balance):
    print(data)
    return '1500'


@router.post("/check_status")
def getFrais(data: schemas.Status):
    print(data)
    return 'SUCCESS'

@router.post("/cashin/yup")
async def cashin(data: schemas.Yup):
    """
    Cashin
    """
    print(data)
    return data


@router.post("/yupGetStatus")
def getFrais(data: schemas.YupGetStatus):
    print(data)
    return 'SUCCESS'


@router.post("/callback")
async def getFrais(request: Request):
    req = await request.json()
    callbacks.append(req)
    f = open('callbacks.txt', 'a')
    f.write(str(req) + '\n')
    f.close()
    print(req)
    return req


@router.get("/callbacks")
def getCallbacks():
    f = open('callbacks.txt', 'r')
    callbacks = f.readlines()
    f.close()
    return callbacks