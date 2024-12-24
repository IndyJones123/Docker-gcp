**How To Dockerize Python**

Create

docker build -t test-mainmodule2 .

docker buildx build -t test-mainmodule3 --platform linux/amd64 . 



















**Testing**

docker run -p 8080:8080 test-mainmodule2
