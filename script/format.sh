#!/bin/bash

USER="$USER"
HOME=/home/$USER
NODE_NAME=node
NODE_NUM=88
HADOOP_HOME=$HOME/hadoop-3.0.0-src/hadoop-dist/target/hadoop-3.0.0
HDFS_TMP_DIR=$HADOOP_HOME/data

stop-dfs.sh

for((i=1;i<=$NODE_NUM;i++));
do
{
    if [[ $i -gt 0 && $i -lt 10 ]]
	then
		host=${NODE_NAME}0${i}
	else
		host=${NODE_NAME}$i
	fi

    echo ---------format $USER@$host start------------

    ssh $USER@$host "cd $HDFS_TMP_DIR; rm -rf ./*"

    echo ---------format $USER@$host finish------------
} &
done

wait

hdfs namenode -format

start-dfs.sh
