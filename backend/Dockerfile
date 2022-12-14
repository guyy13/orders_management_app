FROM python:3.11.0-alpine3.16

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]