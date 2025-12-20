import psutil

cpu_threshold = int(input("Enter threshold value for cpu usage : "))
memory_threshold = int(input("Enter threshold value for memory usage : "))
disk_threshold = int(input("Enter threshold value for disk usage : "))

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

if cpu_threshold > cpu_usage:
    print("cpu threshold is ", cpu_threshold)
else:
    print("cpu usage is ", cpu_usage)

if disk_threshold > disk_usage:
    print("disk threshould is ", disk_threshold)
else:
    print("disk usage is ", disk_usage)

if memory_threshold > memory_usage:
    print("memory threshold is ", memory_threshold)
else:
    print("memory usage is ", memory_usage)
