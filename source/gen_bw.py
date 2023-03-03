import csv
import numpy as np

K = 32
M = 4
F = 4
MAX_BW = 1600.0
U_DIV_B = 2.0
B_BW = MAX_BW / U_DIV_B
B_SCALE = 10

start_idx = 5

bws = []

for j in range((K+M)//F):
    idx = j*F + 1
    np.random.seed()
    temp = np.random.normal(B_BW + B_SCALE, B_SCALE, (1, K + M - F)).tolist()[0]
    bw = []
    i = 0
    for x in range(K + M):
        if (x + 1) >= idx and (x + 1) < idx + F:
            bw.append(MAX_BW)
        else:
            bw.append(temp[i])
            i += 1
    bws.append(bw)

# bw
sfilename = str("bw")+ \
            str("K")+str(K)+ \
            str("M")+str(M)+ \
            str("F")+str(F)+ \
            str("r") +str(int(U_DIV_B)) + \
            str(".csv")
print(sfilename)

with open(sfilename, 'w') as csvwritefile:
    writer = csv.writer(csvwritefile)
    for bw in bws:
        writer.writerow(bw)

