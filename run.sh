#/bin/bash

# for i in $(sudo docker ps -a -q);
#     do sudo docker rm -f $i;
#     done
sudo docker build -t gypscie_core_api:latest .
sudo docker-compose -f docker-compose.yaml up
