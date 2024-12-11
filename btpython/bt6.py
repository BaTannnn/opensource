#!/usr/bin/env python3
with open("data/tritue.txt","r") as f:
    data = f.readlines()
    print(data)
    print(sum(len(line.split()) for line in data))
    print(sum(len(line) for line in data))
    print(data[1] + data[2])
    for i in range(3):
        print(data[i].strip())
