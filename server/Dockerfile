FROM python:3

WORKDIR /server

COPY requiriments.txt .

RUN pip install --no-cache-dir -r requiriments.txt

COPY . .

CMD [ "python", "./app.py" ]
