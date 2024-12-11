#!/bin/bash
ex=$(ls -l $1)
if [ ${ex:9:1} == "x" ]; then
	echo "File da co quyen thuc thi"
else 
	echo -e "File chua co quyen thuc thi.\nVui long doi mot chut....."
	chmod o+x $1
	echo "Da cap quyen thuc thi"
fi
