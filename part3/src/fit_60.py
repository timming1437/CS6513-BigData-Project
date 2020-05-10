import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

no = []
confirm = []
count = 1

with open('data/confirm_processed.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        if (line[0]=='UID'):
            continue
        else:
            for i in range(60,112):
                confirm += [int(line[i])]
                no += [count]
                count += 1

y_data = np.array(confirm)
x_data = np.array(no) 

log_x_data = np.log(x_data)
log_y_data = np.log(y_data)

curve_fit = np.polyfit(x_data, log_y_data, 1)
print(curve_fit)

y = np.exp(6.83351) * np.exp(0.12719027*x_data)
plt.plot(x_data, y_data, "o")
plt.plot(x_data, y)
plt.savefig("images/fit_60.png")
plt.show()