from  scheduling.averages import calculate_avg # import average file for averages(waiting, response, turnaround)

def priority_non_preemptive(processes):

    # be sure column arrival and priority included in table
    for p in processes:
        if "arrival" not in p:
            p["arrival"] = 0

        if "priority" not in p:
            p["priority"] = 1

    # helpers
    time = 0
    completed = 0
    n = len(processes)
    process_table = []
    gantt = []
    last_P_id = None

    # To track start and response time
    start_times = {}
    finish_times = {}

    # Going to all processes 
    while completed < n:
        
        # get all processes that have arrived and that have lower number of proirity(it will be gratest priority)
        ready = [p for p in processes if p["arrival"] <= time and "finished" not in p]

        # no process is available 
        if not ready:
            time += 1
            continue
        
        # take the gratest priority or shortest arrival
        current = min(ready, key=lambda p: (p["priority"], p["arrival"]))
        P_id = current["P_id"]


        if P_id != last_P_id: 
            start_times[P_id] = time

        # add to gantt 
        if P_id != last_P_id:
            gantt.append({
                "P_id": P_id,
                "start" : time
            })
            last_P_id = P_id
        
        time += current["burst"]
        finish_times[P_id] = time
        current["finished"] = True
        completed += 1

    # creat process table
    for p in processes:
            P_id = p["P_id"]
            arrival = p["arrival"]
            burst = p["burst"]
            priority = p["priority"]
            start = start_times[P_id]
            finish = finish_times[P_id]

            waiting = start - arrival
            turnaround = finish - arrival
            response = start - arrival
            process_table.append({
            "P_id": P_id,
            "arrival": arrival,
            "burst": burst,
            "priority": priority,
            "start": start,
            "finish": finish,
            "waiting": waiting,
            "turnaround": turnaround,
            "response": response
        })
            
    # finish the gantt time
    for i in range(len(gantt) - 1):
         gantt[i]["finish"] = gantt[i+1]["start"]
    
    gantt[-1]["finish"] = time

    # calculate averages
    avg = calculate_avg(process_table)

    return{
        "process_table": process_table,
        "gantt_chart": gantt,
        "averages": avg
    }


# # Test code
# processes = [
#     {"P_id": "P1", "arrival": 0, "burst": 7, "priority": 2},
#     {"P_id": "P2", "arrival": 2, "burst": 4, "priority": 1},
#     {"P_id": "P3", "arrival": 4, "burst": 1, "priority": 3},
# ]

# result = priority_non_preemptive(processes)

# print("Process Table:")
# for p in result["process_table"]:
#     print(p)

# print("\nGantt Chart:")
# for g in result["gantt_chart"]:
#     print(g)

# print("\nAverages:")
# print(result["averages"])