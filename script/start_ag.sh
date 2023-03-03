#!/bin/bash

user="$USER"

path=/home/$user/openec/res/openec

redis-cli flushall

sudo service redis_6379 restart

$path/OECAgent