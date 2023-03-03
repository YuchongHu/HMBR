import subprocess
import threading
from time import sleep

vir_dir = "BP-1293369501-172.29.0.100-1655441033937"
hdfs_tmp_dir = "/home/openec/hadoop-3.0.0-src/hadoop-dist/target/hadoop-3.0.0/data/"
append_dir = "dfs/data/current/" + vir_dir + "/current/finalized/subdir1/subdir0/"

start_idx = 1
delete_block_num = 24

hdfs_blocks_dir = hdfs_tmp_dir + append_dir


def format_node_name(node_id):
    return "node{:0>2}".format(node_id)

def rm_blocks(idx):
    ssh_cmd = "ssh openec@" + format_node_name(idx)
    cmd = ssh_cmd + " \"cd " + hdfs_blocks_dir + "; rm ./blk*;\""
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    thread_list = []
    for i in range(delete_block_num):
        thread_list.append(threading.Thread(target=rm_blocks, args=(i+start_idx, )))
    
    cnt = 0
    for i in thread_list:
        print("------------------- " + format_node_name(cnt+start_idx) + " start rm " + " -------------------")
        i.start()
        sleep(0.3)
        print("------------------- " + format_node_name(cnt+start_idx) + " end rm " " -------------------")
        cnt += 1

    
    for i in thread_list:
        i.join()