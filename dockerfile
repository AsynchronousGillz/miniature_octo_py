FROM python:slim

WORKDIR /app

COPY . .

RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]

RUN ["python", "-m", "grpc_tools.protoc", "-I./proto", "--python_out=.", "--grpc_python_out=.", "./proto/miniature/miniature.proto"]

CMD ["python", "-m", "miniature_octo_py"]