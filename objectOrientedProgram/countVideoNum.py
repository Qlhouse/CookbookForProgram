import os
import json

rootDir = r'H:\The Complete Python Course Build 10 Professional OOP Apps\[TutsNode.com] - The Complete Python Course Build 10 Professional OOP Apps'

contentEntry = os.scandir(rootDir)

videoCount = {}

for dir in contentEntry:
    if dir.is_dir():
        os.chdir(dir)
        videoNum = len([name for name in os.listdir(dir)
                       if name.endswith('.mp4')])
        videoCount[os.path.basename(dir)] = videoNum

outputFile = os.path.join(rootDir, 'videoCount.csv')

with open(outputFile, 'w') as f:
    json.dump(videoCount, f)
