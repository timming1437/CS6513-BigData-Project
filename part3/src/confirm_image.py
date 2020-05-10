import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

no = []
confirm = []
count = 0

with open('data/confirm_processed.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        if (line[0]=='UID'):
            continue
        else:
            for i in range(35,112):
                confirm += [int(line[i])]
                no += [count]
                count += 1


df = pd.DataFrame(list(zip(no,confirm)), columns =['no','confirm']) 


plt.plot('no', 'confirm', data=df, marker='', markerfacecolor='blue', linewidth=2, label="confirm")


plt.xlim(0, 80)
plt.ylim(0, 180000)
positions = (0,10,20,30,40,50,60,70)
labels = ("2/15","2/25","3/7","3/17","3/27","4/6","4/16","4/26")
plt.xticks(positions, labels)
plt.legend()
plt.savefig("images/confirm.png")
plt.show()

    

