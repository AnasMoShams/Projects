from  scheduling.averages import calculate_avg # import average file for averages(waiting, response, turnaround)

def round_robin(processes, quantum):

    # Ensure arrival is available
    for p in processes:
        if "arrival" not in p:
            p["arrival"] = 0

    # create remaining burst for each one
    for p in processes:
        p["rem"] = p["burst"]

    # helpers
    time = 0
    completed = 0
    n = len(processes)
    process_table = []
    gantt = []

    # To track start and response time
    start_times = {}
    finish_times = {}

    # Ready queue
    queue = []

    # Sort by arrival first
    processes.sort(key=lambda x: x["arrival"])

    # add first arrivals at time 0
    i = 0
    while i < n and processes[i]["arrival"] <= time:
        queue.append(processes[i])
        i += 1

    last_P_id = None

    # Going to all processes 
    while completed < n:

        if not queue:
            time += 1
            # add new arrivals
            while i < n and processes[i]["arrival"] <= time:
                queue.append(processes[i])
                i += 1
            continue

        current = queue.pop(0)
        P_id = current["P_id"]

        # first response
        if P_id not in start_times:
            start_times[P_id] = time

        # Gantt entry
        if P_id != last_P_id:
            gantt.append({
                "P_id": P_id,
                "start": time
            })
            last_P_id = P_id

        # run for 1 up to quantum
        used = 0
        while used < quantum and current["rem"] > 0:
            current["rem"] -= 1
            time += 1
            used += 1

            # add newly arrived processes
            while i < n and processes[i]["arrival"] <= time:
                queue.append(processes[i])
                i += 1

        # if finished completely
        if current["rem"] == 0:
            finish_times[P_id] = time
            completed += 1
        else:
            # not done → requeue
            queue.append(current)

    # create the process table
    for p in processes:
        P_id = p["P_id"]
        arrival = p["arrival"]
        burst = p["burst"]
        start = start_times[P_id]
        finish = finish_times[P_id]

        waiting = finish - arrival - burst
        turnaround = finish - arrival
        response = start - arrival

        process_table.append({
            "P_id": P_id,
            "arrival": arrival,
            "burst": burst,
            "start": start,
            "finish": finish,
            "waiting": waiting,
            "turnaround": turnaround,
            "response": response
        })

    # finalize gantt
    for i in range(len(gantt)-1):
        gantt[i]["finish"] = gantt[i+1]["start"]
    gantt[-1]["finish"] = time

    avg = calculate_avg(process_table)

    return {
        "process_table": process_table,
        "gantt_chart": gantt,
        "averages": avg
    }


# # Test code
# processes = [
#     {"P_id": "P1", "arrival": 0, "burst": 5},
#     {"P_id": "P2", "arrival": 1, "burst": 3},
#     {"P_id": "P3", "arrival": 2, "burst": 8},
# ]

# result = round_robin(processes, quantum=2)

# print("Process Table:")
# for p in result["process_table"]:
#     print(p)

# print("\nGantt Chart:")
# for g in result["gantt_chart"]:
#     print(g)

# print("\nAverages:")
# print(result["averages"])
