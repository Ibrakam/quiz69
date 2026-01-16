from database import get_db
from database.models import User, UserAnswer, Question, Result



# Функци для добавления
def create_user_db(name, phone_number, level = "easy"):
    db = next(get_db())
    new_user = User(name=name, phone_number=phone_number, level=level)
    db.add(new_user)
    db.commit()
    return True

# Функция получения всех данных из таблицы
def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all() #(User(id=1, ..), User)
    return all_users

# Функция для получения по фильтру
def get_exact_user_db(uid):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=uid).first() #User(id...)
    if exact_user:
        return exact_user
    return False

def get_all_or_exact_user(uid=0):
    db = next(get_db())
    print(db)
    if uid:
        exact_user = db.query(User).filter_by(id=uid).first()
        if exact_user:
            return exact_user
        return False
    all_users = db.query(User).all() 
    return all_users



def save_user_answer_db(uid, qid, user_answer):
    db = next(get_db())
    exact_question = db.query(Question).filter_by(id=qid).first()
    if exact_question:
        if exact_question.correct_answer == user_answer:
            correctness = True
        else:
            correctness = False
        new_answer = UserAnswer(uid=uid, qid=qid, answer=user_answer,
        correctness=correctness)
        db.add(new_answer)
        db.commit()
        if correctness:
            user_result = db.query(Result).filter_by(uid=uid).first()
            if user_result:
                user_result.correct_answers += 1
            else:
                new_result = Result(uid=uid, correct_answers=1)
                db.add(new_result)
            db.commit()
            return True
    return False


def get_user_result_db(uid):
    db = next(get_db())
    user_result = db.query(Result).filter_by(uid=uid).first()
    if user_result:
        return user_result
    return False



