import psutil
# logical=True counts threads, but we are interested in cores
print(psutil.cpu_count(logical=False))

