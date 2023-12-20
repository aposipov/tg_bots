FROM python:3.11

WORKDIR /bot

COPY core_bot .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]