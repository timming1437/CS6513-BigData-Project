import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

date = []
no = []
retial_and_recreation = []
workplaces = []
residential = []
baseline = []
count = 0

with open('data/mobility_processed.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        if (line[0]=='US'):
            no += [count]
            date += line[4]
            retial_and_recreation += [int(line[5])]
            workplaces += [int(line[9])]
            residential += [int(line[10])]
            baseline += [0]
            count += 1

df = pd.DataFrame(list(zip(no,date,retial_and_recreation,workplaces,residential,baseline)), columns =['no','Date','retial_and_recreation','workplaces','residential','baseline']) 


plt.plot('no', 'retial_and_recreation', data=df, marker='', markerfacecolor='blue', linewidth=2, label="retial_and_recreation")
plt.plot('no', 'workplaces', data=df, marker='', color='green', linewidth=2, label="workplaces")
plt.plot('no', 'residential', data=df, marker='', color='yellow', linewidth=2,label="residential")
plt.plot('no', 'baseline', data=df, marker='', color='red', linewidth=1,label="baseline")

plt.xlim(0, 80)
plt.ylim(-80, 40)
positions = (0,10,20,30,40,50,60,70)
labels = ("2/15","2/25","3/7","3/17","3/27","4/6","4/16","4/26")
plt.xticks(positions, labels)
plt.legend()
plt.savefig("images/mobility.png")
plt.show()

    

