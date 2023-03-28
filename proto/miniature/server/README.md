# Generating client and server code

Next you need to generate the gRPC client and server interfaces from your .proto service definition.

Use the following command to generate the Python code:

```shell
python -m grpc_tools.protoc -I../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/route_guide.proto
```


```shell
# 1. Generate CA's private key and self-signed certificate
openssl req -x509 -newkey rsa:4096 -days 365 -nodes -keyout test/data/certs/ca-key.pem -out test/data/certs/ca-cert.pem -subj "/C=us/ST=co/L=denver/O=miniature_octo_py/OU=example/CN=*"

echo "CA's self-signed certificate"
openssl x509 -in ca-cert.pem -noout -text

# 2. Generate web server's private key and certificate signing request (CSR)
openssl req -newkey rsa:4096 -nodes -keyout test/data/certs/server-key.pem -out test/data/certs/server-req.pem -subj "/C=us/ST=co/L=denver/O=miniature_octo_py/OU=example/CN=*"

# 3. Use CA's private key to sign web server's CSR and get back the signed certificate
openssl x509 -req -in test/data/certs/server-req.pem -days 60 -CA test/data/certs/ca-cert.pem -CAkey test/data/certs/ca-key.pem -CAcreateserial -out test/data/certs/server-cert.pem

echo "Server's signed certificate"
openssl x509 -in test/data/certs/server-cert.pem -noout -text
```
