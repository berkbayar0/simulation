import numpy as np

np.random.seed(42)
job_counter = 0
time = 0.0
event_list = []
queue_A = []
queue_B = []
server_A_busy = False
server_B_busy = False
blocked_A = False
blocked_time_total = 0.0
last_time = 0.0

area_queue_A = 0.0
area_queue_B = 0.0
job_stats = []
num_jobs_completed = 0

interarrival = round(np.random.exponential(6), 1)
event_list.append(("arrival", time + interarrival, None))

def schedule_event(event_type, event_time, job_id=None):
    event_list.append((event_type, event_time, job_id))
    event_list.sort(key=lambda x: x[1]) 

def update_areas(current_time):
    global area_queue_A, area_queue_B, last_time
    time_diff = current_time - last_time
    area_queue_A += len(queue_A) * time_diff
    area_queue_B += len(queue_B) * time_diff
    last_time = current_time
    return current_time

while num_jobs_completed < 10:
    event = event_list.pop(0)
    event_type, event_time, job_id = event
    time = update_areas(event_time)

    if event_type == "arrival":
        job_counter += 1
        job_id = job_counter
        queue_A.append((job_id, time))
        interarrival = round(np.random.exponential(6), 1)
        schedule_event("arrival", time + interarrival, None)

        if not server_A_busy and not blocked_A:
            server_A_busy = True
            current_job, arrival_time = queue_A.pop(0)
            process_time = round(np.random.uniform(5, 11), 1)
            schedule_event("end_A", time + process_time, current_job)

    elif event_type == "end_A":
        if len(queue_B) < 2:
            queue_B.append((job_id, time))
            server_A_busy = False
            if queue_A:
                server_A_busy = True
                current_job, _ = queue_A.pop(0)
                process_time = round(np.random.uniform(5, 11), 1)
                schedule_event("end_A", time + process_time, current_job)
            if not server_B_busy:
                schedule_event("start_B", time)
        else:
            blocked_A = True
            blocked_start_time = time
            event_list.insert(0, (event_type, time, job_id))

    elif event_type == "end_block_check":
        if len(queue_B) < 2:
            blocked_A = False
            blocked_duration = time - blocked_start_time
            blocked_time_total += blocked_duration
            server_A_busy = True
            current_job, _ = queue_A.pop(0)
            process_time = round(np.random.uniform(5, 11), 1)
            schedule_event("end_A", time + process_time, current_job)

    elif event_type == "start_B":
        if not server_B_busy and queue_B:
            server_B_busy = True
            current_job, enter_time = queue_B.pop(0)
            process_time = round(np.random.triangular(4, 8, 12), 1)
            schedule_event("end_B", time + process_time, current_job)

    elif event_type == "end_B":
        num_jobs_completed += 1
        server_B_busy = False
        completion_time = time
        job_stats.append(completion_time)

        if queue_B:
            server_B_busy = True
            current_job, enter_time = queue_B.pop(0)
            process_time = round(np.random.triangular(4, 8, 12), 1)
            schedule_event("end_B", time + process_time, current_job)

        if blocked_A:
            schedule_event("end_block_check", time)

total_time = time
avg_queue_A = round(area_queue_A / total_time, 2)
avg_queue_B = round(area_queue_B / total_time, 2)
blocked_percent = round((blocked_time_total / total_time) * 100, 2)
avg_completion_time = round(np.mean(job_stats), 2)

{
    "Average number of jobs at A": avg_queue_A,
    "Average number of jobs at B": avg_queue_B,
    "Percentage of time A is blocked": blocked_percent,
    "Average completion time": avg_completion_time
}
