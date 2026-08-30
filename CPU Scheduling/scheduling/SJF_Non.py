from  scheduling.averages import calculate_avg # import average file for averages(waiting, response, turnaround)

def SJF_non_preemptive(processes):
    # be sure column arrival included in table
    for p in processes:
        if "arrival" not in p:
            p["arrival"] = 0

    # take a copy to work on
    processes = processes.copy()

    # let time = 0 , table and gantt are empty
    time = 0 
    process_table = []
    gantt = []

     # process each task in the dic
    while processes:

        # get all process that have arrived 
        ready_queue = [p for p in processes if p["arrival"] <= time]

        # if no process arrived yet, jump to nex
        if not ready_queue:
            time = min(p["arrival"] for p in processes)
            ready_queue = [p for p in processes if p["arrival"] <= time]

        # take process that have the shortest burst time 
        current = min(ready_queue, key=lambda p: p["burst"])

        P_id = current["P_id"]
        arrival = current["arrival"]
        burst = current["burst"]

        # calculate start and finish times
        start = time
        finish = start + burst

        # calculate waiting, turnaround & response times
        waiting = start - arrival
        turnaround = finish - arrival
        response = waiting

        
        # store result in process table 
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

        # store result in gantt table
        gantt.append({
            "P_id": P_id,
            "start": start,
            "finish": finish
        })

        # move time to the next start 
        time = finish
        # remove the process from list
        processes.remove(current)

        # calculate averages
        avg = calculate_avg(process_table)

    return{
        "process_table": process_table,
        "gantt_chart": gantt,
        "averages": avg
        }
    
# # test the code
# processes = [
#     {"P_id": "P1", "arrival": 0, "burst": 7},
#     {"P_id": "P2", "arrival": 2, "burst": 4},
#     {"P_id": "P3", "arrival": 4, "burst": 1},
# ]
# test = SJF_non_preemptive(processes)
# print("Process Table:")
# for p in test["process_table"]:
#     print(p)
# print("\nGantt Chart:")
# for g in test["gantt_chart"]:
#     print(g)
# print("\nAverages:")
# print(test["averages"])