from fastapi import FastAPI
from api.user_api import user_router
from api.test_api import test_router
from database import Base, engine


app = FastAPI(docs_url="/")

app.include_router(user_router)
app.include_router(test_router)
Base.metadata.create_all(engine)

# uvicorn main:app --reload
