from fastapi import APIRouter
from database.testservice import *

test_router = APIRouter(prefix="/test", tags=["Test API"])


@test_router.post("/add_question")
async def add_question(qtext:str, v1:str, v2:str, correct_answer:str, v3:str=None, v4:str=None, level:str="easy"):
    result = add_question_db(qtext=qtext, v1=v1, v2=v2, correct_answer=correct_answer, v3=v3, v4=v4, level=level)
    return {"status": 1, "message": result}

@test_router.get("/get_20_questions")
async def get_20_question():
    result = get_20_question_db()
    return result

@test_router.get("/get_top_10_users_db")
async def get_top_10_users_db():
    result = get_top_10_users_db()
    return result