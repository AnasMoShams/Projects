

import tkinter as tk
from tkinter import ttk, messagebox
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scheduling.FCFS import FCFS
from scheduling.SJF_preemptive import SJF_preemptive
from scheduling.SJF_Non import SJF_non_preemptive
from scheduling.priority_non_preemptive import priority_non_preemptive
from scheduling.Priority_preemptive import priority_preemptive
from scheduling.RR import round_robin
from scheduling.averages import calculate_avg


def draw_gantt(gantt):
    if not gantt:
        messagebox.showinfo("Gantt Chart", "No Gantt chart to draw.")
        return
    
    fig, ax = plt.subplots(figsize=(12, 3))
    y = 0
    height = 1

    # Random color per PID
    colors = {}
    for g in gantt:
        pid = g["P_id"]
        if pid not in colors:
            colors[pid] = f"#{random.randint(0, 0xFFFFFF):06x}"

    # Draw blocks
    for g in gantt:
        pid = g["P_id"]
        start = g["start"]
        finish = g["finish"]

        ax.add_patch(
            patches.Rectangle(
                (start, y), finish - start, height,
                edgecolor="black",
                facecolor=colors[pid]
            )
        )

        ax.text(
            (start + finish) / 2, y + height / 2, pid,
            ha="center", va="center", fontsize=10, color="white", fontweight="bold"
        )

    # Set x-axis ticks at every integer time
    max_time = max(g["finish"] for g in gantt)
    ax.set_xticks(range(0, max_time + 1))
    ax.set_yticks([])
    ax.set_xlim(0, max_time)
    ax.set_ylim(0, height + 0.5)

    ax.set_xlabel("Time", fontsize=12)
    ax.set_title("Gantt Chart", fontsize=14, fontweight="bold")

    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def start_gui():
    root = tk.Tk()
    root.title("CPU Scheduling GUI")
    root.geometry("1050x500")
    root.resizable(False, False)

    tk.Label(root, text="Scheduler:", font=("Arial", 12, "bold")).place(x=20, y=20)

    scheduler_var = tk.StringVar()
    schedulers =[
        "FCFS",
        "SJF Non-Preemptive",
        "SJF Preemptive",
        "Priority Non-Preemptive",
        "Priority Preemptive",
        "Round Robin"
    ]

    scheduler_menu = ttk.Combobox(root, textvariable=scheduler_var, values=schedulers, state="readonly")
    scheduler_menu.place(x=150, y=20)
    scheduler_menu.current(0)

    tk.Label(root, text="Quantum (RR):", font=("Arial", 12)).place(x=350, y=20)
    quantum_entry = tk.Entry(root, width=5)
    quantum_entry.place(x=450, y=20)


    tk.Label(root, text="P_id").place(x=20, y=70)
    tk.Label(root, text="Arrival").place(x=80, y=70)
    tk.Label(root, text="Burst").place(x=150, y=70)
    tk.Label(root, text="Priority").place(x=220, y=70)

    pid_entry = tk.Entry(root, width=6)
    arrival_entry = tk.Entry(root, width=6)
    burst_entry = tk.Entry(root, width=6)
    priority_entry = tk.Entry(root, width=6)

    pid_entry.place(x=20, y=100)
    arrival_entry.place(x=80, y=100)
    burst_entry.place(x=150, y=100)
    priority_entry.place(x=220, y=100)

    processes = []

    def add_process():
        pid = pid_entry.get()
        arrival = arrival_entry.get()
        burst = burst_entry.get()
        priority = priority_entry.get()

        if not pid or not burst:
            messagebox.showerror("Input Error", "PID and Burst are required.")
            return
        
        try:
            arrival = int(arrival) if arrival else 0
            burst = int(burst)
            priority = int(priority) if priority else 1

        except ValueError:
            messagebox.showerror("Input Error", "Arrival, Burst, and Priority must be integers.")
            return

        processes.append({
            "P_id" : pid,
            "arrival" : arrival,
            "burst" : burst,
            "priority" : priority
        })

        process_table.insert("", "end", values=(pid, arrival, burst, priority))

        pid_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        burst_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)

    tk.Button(root, text="Add Process", command=add_process).place(x=300, y=95)

    process_table = ttk.Treeview(root, columns=("pid", "arr", "burst", "prio"), show="headings", height=10)
    process_table.place(x=20, y=150)

    for col, name in zip(("pid", "arr", "burst", "prio"), ("PID", "Arrival", "Burst", "Priority")):
        process_table.heading(col, text=name)

    
    output = tk.Text(root, width=110, height=13)
    output.place(x=20, y=400)


    def run_scheduler():

        if not processes:
            messagebox.showerror("No Processes", "No processes added. Please add processes first.")
            return
        
        algo = scheduler_var.get()
        data = [p.copy() for p in processes]

        if algo == "FCFS":
            result = FCFS(data)
        elif algo == "SJF Non-Preemptive":
            result = SJF_non_preemptive(data)
        elif algo == "SJF Preemptive":
            result = SJF_preemptive(data)
        elif algo == "Priority Non-Preemptive":
            result = priority_non_preemptive(data)
        elif algo == "Priority Preemptive":
            result = priority_preemptive(data)
        elif algo == "Round Robin":
            q = quantum_entry.get()
            if not q :
                messagebox.showerror("Input Error", "Enter quantum for RR.")
                return
            
            result = round_robin(data, int(q))
        print("Gantt Chart Data:", result["gantt_chart"])


        output.delete("1.0", tk.END)

        output.insert(tk.END, "   PROCESS TABLE  \n")
        for p in result["process_table"]:
            output.insert(tk.END, f"{p}\n")
        
        output.insert(tk.END, "   AVERAGES   \n")
        output.insert(tk.END, f"{result['averages']}\n")

        output.insert(tk.END, "   RAW GANTT   \n")
        for g in result["gantt_chart"]:
            output.insert(tk.END, f"{g}\n")

        draw_gantt(result["gantt_chart"])


    tk.Button(root, text="Run Scheduler", bg="green", fg="white",
              command=run_scheduler).place(x=500, y=95)

    root.mainloop()
