import schema
from fastapi import FastAPI, HTTPException
import subprocess
import os
from filename_generator import generate_unique_filename

app=FastAPI()

@app.post("/evaluation/CPP")
def evaluation(eval: schema.EvaluationCreate):
    script_filename = generate_unique_filename("cpp")
    exe_filename=generate_unique_filename("exe")
    with open(script_filename, 'w') as script_file:
        script_file.write(eval.code)

    try:
        subprocess.run(["g++", f"{script_filename}", "-o", f"{exe_filename}"])
        output=subprocess.run([f"./{exe_filename}"],input=eval.test_case_input.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False)
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
        os.remove(exe_filename)
