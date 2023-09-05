from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import subprocess
import os
from datetime import datetime

def generate_unique_filename():
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"dynamic_code_{current_time}.c++"

#language
class EvaluationCreate(BaseModel):
    code: str
    test_case_input: str
    
    class Config:
        orm_mode = True

app=FastAPI()

@app.post("/evaluation/CPP")
def evaluation(eval: EvaluationCreate):
    script_filename = f"{generate_unique_filename()}"
    with open(script_filename, 'w') as script_file:
        script_file.write(eval.code)
    
    try:
        subprocess.run(["g++", f"{script_filename}", "-o", "my_program"])
        output=subprocess.run(["./my_program"],input=eval.test_case_input.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False)
        if output:
            return {"input":eval.test_case_input,
                    "output": output.stdout,
                    "error": output.stderr}
        else:
            raise HTTPException(status_code=500, detail="Error while executing code")
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        os.remove(script_filename)
