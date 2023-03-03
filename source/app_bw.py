import subprocess
import csv

K = 64
M = 24
F = 24

SCRIPT_PATH = "/home/openec/openec/res/openec/"
SCRIPT_NAME = "limit_bandwidth.sh"

def format_node_name(node_id):
    return "node{:0>2}".format(node_id)

if __name__=='__main__':
    sfilename = str("bw")+ \
            str("K")+str(K)+ \
            str("M")+str(M)+ \
            str("F")+str(F)+ \
            str(".csv")

    with open(sfilename, 'r') as sf:
        reader = csv.reader(sf)
        for row in reader:
            node_id = 1
            for e in row:
                cmd = "ssh {} \"sudo {} {} {}\"".format(format_node_name(node_id), 
                                                SCRIPT_PATH + SCRIPT_NAME,
                                                "all",
                                                format(float(e), '.2f'))
                subprocess.call(cmd, shell=True)
                node_id += 1
    print("ok.")