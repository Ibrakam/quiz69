from fastapi import APIRouter
from database.userservice import *


user_router = APIRouter(prefix="/user", tags=["User API"])


@user_router.post("/add_user")
async def add_user_api(name: str, phone_number: str, 
                        level: str="easy"):
    result = create_user_db(name=name, phone_number=phone_number, 
    level=level)
    return {"status": 1, "message": result}


@user_router.get("/get_all_or_exact_user")
async def get_users_api(uid: int = 0):
    result = get_all_or_exact_user(uid)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": result}



@user_router.post("/user_answer")
async def user_answer_api(uid:int, qid:int, user_answer:str):
    result = save_user_answer_db(uid=uid, qid=qid, user_answer=user_answer)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": result}


@user_router.get("/get_result")
async def get_user_result(uid:int):
    result = get_user_result_db(uid=uid)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": result}

