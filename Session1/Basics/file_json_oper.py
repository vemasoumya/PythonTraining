import json 
with open(r'C:\VSCODEREPOS\Pythontraining\Session1\Basics\Files\Samplefile.json') as json_file:
    data = json.load(json_file)
    for i in data:
        print(i['name'])
        print(i['skills'][0])