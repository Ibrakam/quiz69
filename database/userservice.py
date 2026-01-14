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