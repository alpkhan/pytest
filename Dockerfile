FROM python:3.9

WORKDIR /app

COPY requirements.txt .


COPY . .

CMD [ "python", "Script_run.py" ]
