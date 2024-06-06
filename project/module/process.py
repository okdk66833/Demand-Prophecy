import os

def settingGet():
    currentDir=os.path.dirname(os.path.abspath(__file__))
    settingPath=os.path.join(currentDir,'..','setting')
    with open(settingPath, 'r') as f:
        lines = [f.readline().strip() for _ in range(6)]
    return lines

def settingEdit(input):
    currentDir=os.path.dirname(os.path.abspath(__file__))
    settingPath=os.path.join(currentDir,'..','setting')
    with open(settingPath,'w') as f:
        for line in input:
            line=str(line)
            f.write(line +'\n')

