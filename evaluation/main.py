from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import subprocess
import os

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

    # finally:
    #     os.remove("user_script.py")

# r'"D:\Learning\Vansh\online_judge\evaluation\user_script.py"'
# "D:\\Learning\\Vansh\\online_judge\\evaluation\\user_script.py"

# os.path.join("D:","learning","Vansh","online_judge","evaluation","user_script.py")

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import subprocess

# app = FastAPI()

# class CodeRequest(BaseModel):
#     code: str
#     arguments: list

# @app.post("/evaluation/")
# async def execute_code(code_request: CodeRequest):
#     # Write the received code to a Python file
#     code_file_path = "dynamic_code.py"
#     with open(code_file_path, 'w') as code_file:
#         code_file.write(code_request.code)

#         print(code_request.arguments)

#     try:
#         # Execute the Python file with the provided arguments
#         process = subprocess.Popen(
#             [echo code_request.arguments | "python" code_file_path]
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True
#         )
#         stdout, stderr = process.communicate()

#         # Check if the execution was successful
#         if process.returncode == 0:
#             return {"output": stdout}
#         else:
#             raise HTTPException(status_code=500, detail=f"Error executing code:\n{stderr}")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     # finally:
#     #     # Clean up the temporary code file
#     #     subprocess.run(["rm", code_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)