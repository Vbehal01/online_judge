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
        compile_process=subprocess.run(["g++", f"{script_filename}", "-o",f"{exe_filename}"], stderr=subprocess.PIPE)
        if compile_process.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Compilation_error: {compile_process.stderr}")
        
        else:
            output=subprocess.run([f"./{exe_filename}"],input=eval.test_case_input.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False)
            result=output.stdout
            result=result.decode()
            result=result.rstrip('\n').rstrip('\r')
            if output.returncode != 0:
                raise HTTPException(status_code=500, detail=f"Runtime_error: {output.stderr}")
            else:
                os.remove(exe_filename)
                return {"input":eval.test_case_input,
                        "output": result}
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        os.remove(script_filename)
