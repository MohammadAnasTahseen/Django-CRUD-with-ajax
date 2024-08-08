import psutil

def monitor_system_resources():
    # Get RAM usage
    ram_usage = psutil.virtual_memory()
    print(f"RAM Usage: {ram_usage.percent}%")

    # Get CPU usage
    cpu_usage = psutil.cpu_percent()
    print(f"CPU Usage: {cpu_usage}%")

    # Get running processes
    running_processes = psutil.process_iter()
    print(f"Running Processes: {len(list(running_processes))}")