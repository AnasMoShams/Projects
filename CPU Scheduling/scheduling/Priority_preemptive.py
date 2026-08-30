from  scheduling.averages import calculate_avg # import average file for averages(waiting, response, turnaround)

def priority_preemptive(processes):

    # be sure culomns arrival and priority in table
    for p in processes:
        if "arrival" not in p:
            p["arrival"] = 0
        if "priority" not in p:
            p["priority"] = 1

    # create remaining burst for each one
    for p in processes:
        p["rem"] = p["burst"]

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
        
        # get all processes that have arrived and remaining biger then 0
        ready = [p for p in processes if p["arrival"] <= time and p["rem"] > 0]

        if not ready:
            time += 1
            continue

        current = min(ready, key=lambda p: (p["priority"], p["arrival"]))
        P_id = current["P_id"]

        if P_id not in start_times:
            start_times[P_id] = time

        if P_id != last_P_id:
            gantt.append({
                "P_id" : P_id,
                "start" : time
            })
            last_P_id = P_id

        current["rem"] -= 1
        time += 1

        if current["rem"] == 0:
            finish_times[P_id] =time
            completed += 1

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
            
    for i in range(len(gantt) - 1):
         gantt[i]["finish"] = gantt[i+1]["start"]
    
    gantt[-1]["finish"] = time

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

# result = priority_preemptive(processes)

# print("Process Table:")
# for p in result["process_table"]:
#     print(p)

# print("\nGantt Chart:")
# for g in result["gantt_chart"]:
#     print(g)

# print("\nAverages:")
# print(result["averages"])
