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

        
    try:
        output = subprocess.check_output(["echo", eval.test_case_input, "|", "python", "D:\\Learning\\Vansh\\online_judge\\evaluation\\user_script.py"], stderr=subprocess.STDOUT, text=True, shell=True).rstrip('\n')
        if output:
            return {"input":eval.test_case_input,
                    "output": output}
        else:
            raise HTTPException(status_code=500, detail="Error while executing code")
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
DEFAULT_PORT = 8080

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=DEFAULT_PORT)
