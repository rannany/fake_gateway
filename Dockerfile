FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pipenv wheel && pipenv install

CMD [ "python", "main.py" ]