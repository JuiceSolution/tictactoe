import json

mcdata = {}

with open("Morris-Code.txt") as f:
    mcdata = f.readlines()

print(mcdata)