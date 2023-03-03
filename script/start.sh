#!/bin/bash

user="$USER"
node_num=80
node_name=node

home=/home/$user
hadoop_home=$home/hadoop-3.0.0-src/hadoop-dist/target/hadoop-3.0.0

remote_path=/home/$user/openec/res/openec

cmake . -DFS_TYPE:STRING=HDFS3

make

./autoSync.sh

cp ./hdfs3-integration/conf/* $hadoop_home/etc/hadoop/

./format.sh

if [ -f "entryStore" ];
then
    rm entryStore
fi

if [ -f "poolStore" ];
then
    rm poolStore
fi

redis-cli flushall

sudo service redis_6379 restart

./OECCoordinator &

sleep 2

for((i=1;i<=$node_num;i++));
do
{
    i=$i
	if [[ $i -gt 0 && $i -lt 10 ]]
	then
		host=${node_name}0${i}
	else
		host=${node_name}$i
	fi

    ssh $user@$host "source /etc/profile; cd $remote_path; ./start_ag.sh;"
	sleep 0.5
}
done
