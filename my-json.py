import json
from doc import file

dict_to_json = json.dumps(file)
print(dict_to_json)

with open('dict_to_json.txt','w') as f:
    json.dump(file,f)

