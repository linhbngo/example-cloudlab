#!/bin/bash
set -x
sudo bash -c "echo 'export HADOOP_HOME=/opt/hadoop-3.1.1/' >> /etc/profile"
sudo bash -c "echo 'export PATH=$HADOOP_HOME/bin:$PATH' >> /etc/profile"
