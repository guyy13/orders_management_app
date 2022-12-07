FROM python:3.11.0-alpine3.16

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "app.py" ]