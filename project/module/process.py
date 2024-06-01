import os

def settingGet(input):
    currentDir=os.path.dirname(os.path.abspath(__file__))
    settingPath=os.path.join(currentDir,'..','setting')
    with open(settingPath, 'r') as f:
        lines = [f.readline().strip() for _ in range(6)]

    if input=="tabview":
        return [lines[0],lines[1],lines[2],lines[3]]

def settingEdit(input):
    currentDir=os.path.dirname(os.path.abspath(__file__))
    settingPath=os.path.join(currentDir,'..','setting')
    pass
