#!/bin/bash
set -x

sudo cp /local/repository/hadoop-env.sh /opt/hadoop-3.1.1/etc/hadoop/hadoop-env.sh

#sudo sed -i -e "s/HOSTNAME/$(sudo ssh -o StrictHostKeyChecking=no root@namenode hostname)/g" /local/repository/core-site.xml
sudo cp /local/repository/core-site.xml /opt/hadoop-3.1.1/etc/hadoop/core-site.xml

#sudo sed -i -e "s/HOSTNAME/$(sudo ssh -o StrictHostKeyChecking=no root@namenode hostname)/g" /local/repository/yarn-site.xml
sudo cp /local/repository/yarn-site.xml /opt/hadoop-3.1.1/etc/hadoop/yarn-site.xml
