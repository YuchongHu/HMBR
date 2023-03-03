#!/bin/bash

user="$USER"
node_num=88
node_name=node

echo ------------clean bandwidth limited-------------

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

    echo ------------clean agent$i-------------
    ssh $user@$host "sudo /home/openec/openec/res/openec/limit_bandwidth.sh all 1600"
} &
done

wait 