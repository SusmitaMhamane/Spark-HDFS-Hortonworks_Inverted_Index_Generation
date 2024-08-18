#!/bin/bash
#
# Author: Susmita Mhamane
# Date: 8 June 2024
#

source ./unset_jupyter.sh
hdfs dfs -test -e /user/talentum/hortonworks.txt
if [ $? -eq 0 ]; then
    echo "File is There"
    hdfs dfs -rm /user/talentum/hortonworks.txt
    echo "File Deleted Successfully"
fi
echo "Putting file on HDFS"
hdfs dfs -put ~/shared/hortonworks.txt /user/talentum/
echo "File copied successfully."
spark-submit hortonworks.py
