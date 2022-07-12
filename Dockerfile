FROM python:slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]

COPY ./ ./

CMD ["python", "-m", "miniature_octo_py"]