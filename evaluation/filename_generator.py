import uuid
def generate_unique_filename(extension: str):
    filename = uuid.uuid4().hex
    return f"{filename}.{extension}"
