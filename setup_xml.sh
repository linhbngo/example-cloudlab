#!/bin/bash
set -x

sudo /bin/cp -rf /local/repository/xml/hadoop-env.sh /opt/hadoop-3.1.1/etc/hadoop/hadoop-env.sh

sudo /bin/cp -rf /local/repository/xml/core-site.xml /opt/hadoop-3.1.1/etc/hadoop/core-site.xml

sudo /bin/cp -rf /local/repository/xml/yarn-site.xml /opt/hadoop-3.1.1/etc/hadoop/yarn-site.xml

sudo /bin/cp -rf /local/repository/xml/mapred-site.xml /opt/hadoop-3.1.1/etc/hadoop/mapred-site.xml

sudo /bin/cp -rf /local/repository/xml/hdfs-site.xml /opt/hadoop-3.1.1/etc/hadoop/hdfs-site.xml
