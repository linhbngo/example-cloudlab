#!/bin/bash
set -x
sudo su
if hostname | grep -q namenode; then
  /opt/hadoop-3.1.1/bin/hdfs namenode -format CloudLab-Hadoop
  /opt/hadoop-3.1.1/bin/hdfs --daemon start namenode
  /opt/hadoop-3.1.1/bin/yarn --daemon start resourcemanager
  /opt/hadoop-3.1.1/bin/hdfs dfs -mkdir /user
  /opt/hadoop-3.1.1/bin/hdfs dfs -mkdir /tmp
  /opt/hadoop-3.1.1/bin/hdfs dfs -mkdir /tmp/hadoop-yarn
  /opt/hadoop-3.1.1/bin/hdfs dfs -mkdir /tmp/hadoop-yarn/staging
  /opt/hadoop-3.1.1/bin/hdfs dfs -chmod 1777 /tmp
  /opt/hadoop-3.1.1/bin/hdfs dfs -chmod 1777 /tmp/hadoop-yarn
  /opt/hadoop-3.1.1/bin/hdfs dfs -chmod 1777 /tmp/hadoop-yarn/staging
fi
