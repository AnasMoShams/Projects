from collections import deque # import queue
from  scheduling.averages import calculate_avg # import average file for averages(waiting, response, turnaround)


def FCFS(processes):
    # be sure column arrival included in table
    for p in processes:
        if "arrival" not in p:
            p["arrival"] = 0

    # sort tabel by arrival then stor in queue
    processes = sorted(processes, key=lambda p: p["arrival"])
    q = deque(processes)
    
    # let time = 0 , table and gantt are empty
    time = 0
    process_table = []
    gantt = []

    # process each task in the queue
    while q:
        p = q.popleft()

        P_id = p["P_id"]
        arrival = p["arrival"]
        burst = p["burst"]

        # wait process arrives 
        if time < arrival:
            time = arrival

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

    # calculate average matrics 
    avg = calculate_avg(process_table)

    # return all result
    return {
        "process_table": process_table,
        "gantt_chart": gantt,
        "averages": avg
    }


# # test the code
# processes = [
#     {"P_id": "P1", "burst": 5},
#     {"P_id": "P2", "burst": 3},
# ]
# test = FCFS(processes)
# print("processes table: ")
# for p in test["process_table"]:
#     print(p)


# print("\nGantt chart: ")
# for g in test["gantt_chart"]:
#     print(g)

# print("\nAverages: ")
# print(test["averages"])
