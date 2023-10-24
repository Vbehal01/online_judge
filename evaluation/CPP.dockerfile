FROM python:3.9
RUN apt-get update && apt-get install -y build-essential
WORKDIR /app
COPY cpp.py /app/
COPY filename_generator.py /app/
COPY schema.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 8001
CMD ["uvicorn", "cpp:app", "--host", "0.0.0.0", "--port", "8001"]
