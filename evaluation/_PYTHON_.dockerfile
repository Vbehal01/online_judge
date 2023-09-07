FROM python:3.9
WORKDIR /app
COPY _PYTHON_.py /app/
COPY filename_generator.py /app/
COPY schema.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

CMD ["uvicorn", "_PYTHON_:app", "--host", "0.0.0.0", "--port", "8001"]