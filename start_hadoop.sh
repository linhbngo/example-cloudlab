#!/bin/bash
set -x
sudo su
if hostname | grep -q namenode; then
  hdfs namenode -format CloudLab-Hadoop
  hdfs --daemon start namenode
  yarn --daemon start resourcemanager
  hdfs dfs -mkdir /user
  hdfs dfs -mkdir /tmp
  hdfs dfs -mkdir /tmp/hadoop-yarn
  hdfs dfs -mkdir /tmp/hadoop-yarn/staging
  hdfs dfs -chmod 1777 /tmp
  hdfs dfs -chmod 1777 /tmp/hadoop-yarn
  hdfs dfs -chmod 1777 /tmp/hadoop-yarn/staging
fi
