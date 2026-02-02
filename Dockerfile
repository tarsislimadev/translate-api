FROM python:3.12.12

RUN pip install argostranslate

RUN pip install argostranslategui

RUN pip install flask

WORKDIR /app

COPY . .

CMD flask --app main run
