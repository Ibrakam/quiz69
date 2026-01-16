from sqlalchemy import desc
from database import get_db
from database.models import Question, Result



def add_question_db(qtext, v1, v2, correct_answer, v3=None, v4=None, level="easy"):
    db = next(get_db())
    new_question = Question(qtext=qtext, v1=v1, v2=v2, v3=v3, v4=v4, 
    correct_answer=correct_answer, level=level)
    db.add(new_question)
    db.commit()
    return True


def get_20_question_db():
    db = next(get_db())
    all_questions = db.query(Question).all()
    return all_questions[:20]


def get_top_10_users_db():
    db = next(get_db())
    result = db.query(Result).order_by(desc(Result.correct_answers)).all()[:10]
    return result
