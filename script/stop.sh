#!/bin/bash

user="$USER"
node_num=88
node_name=node

echo ------------stop coordinator-------------
redis-cli flushall
killall OECCoordinator

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

    echo ------------stop agent$i-------------
    ssh $user@$host "killall OECAgent; redis-cli flushall"
} &
done

wait