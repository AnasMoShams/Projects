def calculate_avg(process_table):
    # to know the length for table
    n = len(process_table)

    # calculat the averages 
    avg_waiting = sum(p["waiting"] for p in process_table) / n
    avg_turnaround = sum(p["turnaround"] for p in process_table) / n 
    avg_response = sum(p["response"] for p in process_table) / n

    # the result for calculating averages
    return {
        "avg_waiting_time": round(avg_waiting, 2),
        "avg_turnaround_time": round(avg_turnaround, 2),
        "avg_response_time": round(avg_response, 2),
    }



