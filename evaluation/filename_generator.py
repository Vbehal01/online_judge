import uuid
def generate_unique_filename():
    filename = uuid.uuid4().hex
    return f"{filename}.c++"

def generate_unique_exename():
    exename = uuid.uuid4().hex
    return f"{exename}.exe"
