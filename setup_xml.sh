#!/bin/bash
set -x

sudo /bin/cp -rf /local/repository/hadoop-env.sh /opt/hadoop-3.1.1/etc/hadoop/hadoop-env.sh

sudo /bin/cp -rf /local/repository/core-site.xml /opt/hadoop-3.1.1/etc/hadoop/core-site.xml

sudo /bin/cp -rf /local/repository/yarn-site.xml /opt/hadoop-3.1.1/etc/hadoop/yarn-site.xml

sudo /bin/cp -rf /local/repository/mapred-site.xml /opt/hadoop-3.1.1/etc/hadoop/mapred-site.xml
