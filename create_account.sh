#!/bin/bash
set -x
sudo su
bash -c "echo 'export HADOOP_HOME=/opt/hadoop-3.1.1/' >> /etc/profile"
bash -c "echo 'export PATH=/opt/hadoop-3.1.1/bin:$PATH' >> /etc/profile"

source /etc/profile
cd /users
i=0
while read line
do
  array[ $i ]="$line"
  (( i++ ))
done < <(find . -mindepth 1 -maxdepth 1 -type d \( ! -iname ".*" \) | sed 's|^\./||g')

groupadd hadoop

for j in "${array[@]}"
do
  usermod -a -G hadoop $j
  hdfs dfs -mkdir -p /user/$j
  hdfs dfs -chown $j:hadoop /user/$j
  sudo hdfs dfs -chmod 755 /user/$j
done

