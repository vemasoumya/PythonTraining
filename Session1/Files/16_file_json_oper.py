import json 
with open(r'C:\VSCODEREPOS\Pythontraining\Session1\Files\TestFiles\Samplefile.json') as json_file:
    data = json.load(json_file)
    for i in data:
        print(i['name'])
        print(i['skills'][0])