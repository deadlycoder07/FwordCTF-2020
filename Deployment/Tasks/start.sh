#!/bin/bash
echo "[!] Run me with sudo pleaaaaase!"
docker run -it --name registry -p 127.0.0.1:5000:5000 -d registry:2
if [ $? -eq 0 ]; then
echo "[+] registry done!"
else
    echo "Failed"
fi
docker-compose -f docker-compose-sample.yml build
docker-compose -f docker-compose-sample.yml push
if [ $? -eq 0 ]; then
  echo "[+] Image pushed!"
else
    echo FAILED
fi
docker swarm init
docker stack deploy --compose-file docker-compose-sample.yml task
if [ $? -eq 0 ]; then
echo "[+] Done, Fword FTW"
else
    echo FAILED
fi
