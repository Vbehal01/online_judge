FROM python:3.9
WORKDIR /app
COPY CPP.py /app/
COPY filename_generator.py /app/
COPY schema.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

CMD ["uvicorn", "CPP:app", "--host", "0.0.0.0", "--port", "8002"]