FROM python:3.10

WORKDIR /pipeline

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "pipeline.py"]
