FROM python:3.11

WORKDIR /usr/src/app

COPY srcs .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "bot_test.py" ]