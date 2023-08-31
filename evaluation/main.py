from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import subprocess
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

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
    # logging.info(f"enter evaluation: {eval}")
    script_filename = f"{generate_unique_filename()}"
    with open(script_filename, 'w') as script_file:
        script_file.write(eval.code)

    script_path=os.path.abspath(script_filename).replace('\\','\\\\')
    logging.info(f"path: {script_path}")
    
        
    try:
        # output1 = subprocess.check_output(["echo", eval.test_case_input], stderr=subprocess.STDOUT, text=True, shell=True)
        # logging.info(f"output1 is before {output1}")
        # output1=output1.rstrip('\n')
        # logging.info(f"outpu1 is {output1}")

        # output2 = subprocess.check_output(["python", f"{script_path}"], stderr=subprocess.STDOUT, text=True, shell=True)
        # logging.info(f"output2 is before {output2}")
        # output2=output2.rstrip('\n')
        # logging.info(f"output2 is {output2}")
        
        output = subprocess.check_output(["echo", eval.test_case_input, "|", "python", f"{script_path}"], stderr=subprocess.STDOUT, text=True, shell=True)
        # logging.info(f"testcase input is {eval.test_case_input}")
        # logging.info(f"output is before {output}")
        output=output.rstrip('\n')
        # logging.info(f"output is {output}")
        if output:
            return {"input":eval.test_case_input,
                    "output": output}
        else:
            raise HTTPException(status_code=500, detail="Error while executing code")
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        os.remove(script_filename)
    # except Exception as e:
    # print("an error occured",e)
