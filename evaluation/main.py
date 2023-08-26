from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import subprocess
import os
import uvicorn

#language
class EvaluationCreate(BaseModel):
    code: str
    test_case_input: str
    
    class Config:
        orm_mode = True


app=FastAPI()

@app.post("/evaluation/")
def evaluation(eval: EvaluationCreate):
    script_filename = "user_script.py"
    with open(script_filename, 'w') as script_file:
        script_file.write(eval.code)
    
    script_path=os.path.abspath(script_filename).replace('\\','\\\\')
    print(f"{script_path}")

        # "D:\\Learning\\online_judge\\evaluation\\user_script.py"
    try:
        print(eval.test_case_input)
        output = subprocess.check_output(["echo", eval.test_case_input, "|", f"{script_path}"], stderr=subprocess.STDOUT, text=True, shell=True).rstrip('\n')
        print(output)
        if output:
            return {"input":eval.test_case_input,
                    "output": output}
        else :
            raise HTTPException(status_code=500, detail="Error while executing code")
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(script_filename)
