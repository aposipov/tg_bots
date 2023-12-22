FROM python:3.11

WORKDIR /bot

COPY core_bot .

RUN pip install --upgrade pip &&  \
    pip install --no-cache-dir -r requirements.txt && \
    sed -i '42d' /usr/local/lib/python3.11/site-packages/g4f/Provider/__init__.py

CMD [ "python", "main.py" ]