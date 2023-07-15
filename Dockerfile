FROM python:3.9

WORKDIR /app

COPY requirements.txt .


COPY . .

CMD [ "python", "placeholder_script.py" ]
