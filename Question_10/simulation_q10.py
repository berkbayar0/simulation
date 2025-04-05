import numpy as np

num_days = 200
patients_per_day = 16
day_minutes = 480  
appointment_times = np.arange(0, patients_per_day * 30, 30)

arrival_shift_choices = [-15, -5, 0, 10, 15]
arrival_shift_probs = [0.10, 0.25, 0.50, 0.10, 0.05]

exam_durations = [24, 27, 30, 33, 36, 39]
exam_probs = [0.20, 0.25, 0.30, 0.10, 0.10, 0.05]

all_no_wait_counts = []
last_patient_no_waits = []
utilization_rates = []

for _ in range(num_days):
    doctor_free_time = 0
    no_wait_count = 0
    total_work_time = 0
    last_patient_waited = True

    for i in range(patients_per_day):
        appointment_time = appointment_times[i]
        arrival_shift = np.random.choice(arrival_shift_choices, p=arrival_shift_probs)
        arrival_time = appointment_time + arrival_shift

        exam_duration = np.random.choice(exam_durations, p=exam_probs)
        start_time = max(arrival_time, doctor_free_time)
        wait_time = start_time - arrival_time
        end_time = start_time + exam_duration

        if wait_time == 0:
            no_wait_count += 1
            if i == patients_per_day - 1:
                last_patient_waited = False
        elif i == patients_per_day - 1:
            last_patient_waited = True

        total_work_time += exam_duration
        doctor_free_time = end_time

    all_no_wait_counts.append(no_wait_count)
    last_patient_no_waits.append(0 if last_patient_waited else 1)
    utilization_rates.append(total_work_time / day_minutes)

avg_no_wait_prob = np.mean([x / patients_per_day for x in all_no_wait_counts])
last_patient_prob = np.mean(last_patient_no_waits)
avg_utilization = np.mean(utilization_rates)

print("Probability a patient does not wait:", round(avg_no_wait_prob, 3))
print("Probability the last patient does not wait:", round(last_patient_prob, 3))
print("Average doctor utilization:", round(avg_utilization, 3))
