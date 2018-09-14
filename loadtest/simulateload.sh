#!/bin/bash
while :
do
	curl "http://localhost:5000/?search=Dockr" > /dev/null
	sleep 2
    curl "http://localhost:5000/?tags=Coding+Blocks" > /dev/null
    sleep 2
    curl "http://localhost:5000/?tags=Coding+Blocks&search=fff"  > /dev/null # this throws an exception!
    sleep 2
    curl "http://localhost:5000/?search=$RANDOM" > /dev/null
    sleep 2
done