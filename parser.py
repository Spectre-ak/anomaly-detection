log=open("./loghub/HDFS/HDFS_2k.log")
count=0

cleaned_log=open("./hdfs_c.log","w")

for f in log:
    arr=f.split(" ")
    arr=arr[3:]
    cleaned_log.write(" ".join(arr))