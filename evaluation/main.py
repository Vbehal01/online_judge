import schema
from fastapi import FastAPI, HTTPException
import subprocess
import os
from filename_generator import generate_unique_filename

app=FastAPI()

try:
    @app.post("/evaluation/python")
    def evaluation(eval: schema.EvaluationCreate):
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
except Exception as e:
    print("an error occured",e)
