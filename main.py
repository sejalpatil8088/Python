from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Hello World"}

class ChoiceBase(BaseModel):
   choice_text: str
   is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/questions")
async def create_question(question: QuestionBase, db: db_dependency):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = models.Choices(choice_text=choice.choice_text, is_correct=choice.is_correct, question_id=db_question.id)
        db.add(db_choice)
    db.commit()   
# bank_account = 200
# proper_towels = 20
# water = 10

# bank_account = bank_account - proper_towels
# bank_account = bank_account - water
# print(bank_account)

# first_name = "John"
# last_name = "Doe"
# full_name = first_name + " " + last_name
# print(full_name)

# second assignment
# item1 = "phone"
# item2 = "watch"
# item3 = "laptop"
# print(f"In my birthday i want {item1}, {item2}, {item3}")

# number = 100
# if number > 100:
#     print("The number is greater than 100")
    
# print("App ended")

# loop
# numbers = [1, 2, 3, 4, 5]
# for i in range(0 , 11):
#     print(i)

# trules and sets
# my_tuples = (1, 2, 3, 4, 5)
# print(my_tuples[2])

# def my_first_function(first_name , last_name):
#     print(f"Hello my name is {first_name} {last_name}")
    
# my_first_function("sejal" , "patil")

# grade = 70
# if(grade >= 90):
#     print("A")
# elif(grade >= 80):
#     print("B")
# elif(grade >= 70):
#     print("C")
# elif(grade >= 60):
#     print("D")
# else:
#     print("F")

# time = 10
# if time <= 14:
#     print("Good morning")
# elif time <= 18:
#     print("Good afternoon")
# else:
#     print("Good evening")
   
# colors = ["red", "blue", "green", "yellow"]
# colors.append("white")
# print(colors)

# from fastapi import FastAPI,HTTPException,Depends
# from pydantic import BaseModel
# from typing import List,Annotated
# import models
# from database import engine, SessionLocal
# from sqlalchemy.orm import Session
# app = FastAPI()
# models.Base.metadata.create_all(bind=engine) # this line is going to create all columns in the postgres
# class ChoiceBase(BaseModel):
#     choice_text:str
#     is_correct:bool
# class QuestionBase(BaseModel):
#     question_text:str
#     choices:List[ChoiceBase]
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# db_dependency = Annotated[Session,Depends(get_db)]
# #http://127.0.0.1:8000/docs  Swagger Documentation
# @app.get("/questions/{question_id}")
# async def read_question(question_id:int,db:db_dependency):
#     result=db.query(models.Questions).filter(models.Questions.id == question_id).first()
#     if not result:
#         raise HTTPException(status_code=404,detail='Question is not found')
#     return result
# @app.get("/choices/{question_id}")
# async def read_choices(question_id:int,db:db_dependency):
#     result = db.query(models.Choices).filter(models.Choices.question_id == question_id).all()
#     if not result:
#         raise HTTPException(status_code=404,detail='No Choices Found')
#     return result
# @app.post("/questions")
# async def create_questions(question:QuestionBase,db:db_dependency):
#     db_question = models.Questions(question_text = question.question_text)
#     db.add(db_question)
#     db.commit()
#     db.refresh(db_question)
#     for choice in question.choices:
#         db_choice = models.Choices(choice_text = choice.choice_text,is_correct=choice.is_correct,question_id=db_question.id)
#         db.add(db_choice)
#     db.commit()
# # http://127.0.0.1:8000/docs#/default/create_questions_questions_post






