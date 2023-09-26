with  open(r'C:\VSCODEREPOS\Pythontraining\Session1\Files\TestFiles\SampleFile1.txt') as file:
    for i in file:
        print(i)

lines = ['Readme', 'How to write text files in Python']
with open('samplewrite.txt', 'w') as f:    
    for line in lines:
        f.write(line)
        f.write('\n')