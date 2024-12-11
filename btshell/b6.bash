#!/bin/bash
for i in $(seq 10 $((10+$2))); do
	echo "$1$i.txt"
done
