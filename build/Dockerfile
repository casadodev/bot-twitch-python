FROM python:3

WORKDIR /usr/src/app

COPY ../deps.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ../ .

CMD [ "python", "./bot.py" ]