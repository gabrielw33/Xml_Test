import requests
import re
import json
import sys


if len(sys.argv) < 2 :
    print("Error : no parameter")
else:    
    url = sys.argv[1]

responce = requests.get(url)
dictionary = {}
reg = r"(([A-Z]\w+\.)+((\d-\d\.)|[A-Z]\w+\.)+((\d-\d\.)|[A-Z]\w+))"
match = re.finditer(reg, responce.text)

for matchNum, match in enumerate(match, start=1):
  
    key = match.group()
    dictionary[key] = -2
    

json = json.dumps(dictionary,indent=4)
f = open("dict2.json","w")
f.write(json)
f.close()



