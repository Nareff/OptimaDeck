FROM python:3.9

ENV SECRET_KEY="hardcoded_insecure_key"

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
