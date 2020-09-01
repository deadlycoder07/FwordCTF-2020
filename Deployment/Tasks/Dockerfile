version: "3.8"
services:
  task:
    image: 127.0.0.1:5000/task
    build:
      context: .
      dockerfile: ./Dockerfile
    container_name: taskName
    deploy:
      mode: replicated
      replicas: 3
    networks:
      - isolated
    ports:
      - "9999:1234" #ToChange
networks:
  isolated:
