#!/bin/bash

set -x
sudo wget http://apache.cs.utah.edu/hadoop/common/hadoop-3.1.1/hadoop-3.1.1.tar.gz
sudo tar xzf hadoop-3.1.1.tar.gz -C /opt/
sudo apt-get update -y
sudo apt-get install -y default-jdk
