from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import subprocess
import os
from datetime import datetime
import uvicorn

def generate_unique_filename():
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"dynamic_code_{current_time}.py"

#language
class EvaluationCreate(BaseModel):
    code: str
    test_case_input: str
    
    class Config:
        orm_mode = True

app=FastAPI()

@app.post("/evaluation/")
def evaluation(eval: EvaluationCreate):
    script_filename = f"{generate_unique_filename()}"
    with open(script_filename, 'w') as script_file:
        script_file.write(eval.code)

    script_path=os.path.abspath(script_filename).replace('\\','\\\\')
        
    try:
        output = subprocess.check_output(["echo", eval.test_case_input, "|", "python", f"{script_path}"], stderr=subprocess.STDOUT, text=True, shell=True).rstrip('\n')
        if output:
            return {"input":eval.test_case_input,
                    "output": output}
        else:
            raise HTTPException(status_code=500, detail="Error while executing code")
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        os.remove(script_filename)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
