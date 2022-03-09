#%%

import requests
import json
import zlib
import pickle

with open('workflow_ex.json', 'r') as file:
    fluxo = json.loads(file.read())
# %%
response = requests.post(
    'http://localhost:6057', 
    data=json.dumps(fluxo),
    headers={'Content-Type': 'application/json'},
    )

print(response.json())