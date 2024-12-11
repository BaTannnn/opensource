#!/bin/bash
directory="$1"
if [ -d $directory ]; then
	echo "Thu muc co ton tai"
else 
	echo "Thu muc khong co ton tai"
fi
