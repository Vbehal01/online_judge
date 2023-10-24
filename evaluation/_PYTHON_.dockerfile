FROM python:3.9
WORKDIR /app
COPY _python_.py /app/
COPY filename_generator.py /app/
COPY schema.py /app/
COPY requirements.txt /app/
EXPOSE 8002
RUN pip install -r requirements.txt

CMD ["uvicorn", "_python_:app", "--host", "0.0.0.0", "--port", "8002"]