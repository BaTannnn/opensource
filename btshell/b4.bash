#!/bin/bash
# bài 7 

read -p "Nhap duong dan thu muc: " dir
read -p "Nhap loai file can xoa: " exten

if [ ! -d "$dir" ]; then
	echo "Thu muc khong ton tai"
	exit 1
fi
files=$(find "$dir" -type f -name "*.$exten" 2>/dev/null)
if [ -z "$files" ]; then
    echo "Không có file .$exten trong thư mục '$dir'."
    exit 0
else
	echo "$files"
fi
for file in $files; do
	rm "$file"
done
