from pydantic import BaseModel
from fastapi import FastAPI
import os

#language
class EvaluationBase(BaseModel):
    pass

class EvaluationCreate(EvaluationBase):
    pass

class Evaluation(EvaluationBase):
    output:str
    
    class Config:
        orm_mode = True


code='''def sum_of_two_numbers(a, b):
    return a + b

num1 = float(input())
num2 = float(input())

result = sum_of_two_numbers(num1, num2)
print(f"{result}")'''

test_case_input='1/n1'

app=FastAPI()

@app.post("/evaluation/",response_model=Evaluation)
def evaluation(code: str, test_case_input: str):
    file_name="temporary_file.py"
    with open(file_name,"w") as file:
        file.write(code)

    return os.system(f"python temporary_file.py  {test_case_input}")