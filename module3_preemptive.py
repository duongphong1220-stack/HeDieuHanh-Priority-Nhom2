def priority_preemptive(processes):
    n = len(processes)
    remaining = [p["burst"] for p in processes]
    completion = [0] * n
    current_time = 0
    completed = 0
    gantt = []

    while completed < n:
        selected = -1

        # Tìm tiến trình đã đến (arrival <= current_time), chưa xong,
        # có priority nhỏ nhất; nếu bằng nhau -> ai đến trước chạy trước
        for i in range(n):
            if processes[i]["arrival"] <= current_time and remaining[i] > 0:
                if selected == -1:
                    selected = i
                elif processes[i]["priority"] < processes[selected]["priority"]:
                    selected = i
                elif processes[i]["priority"] == processes[selected]["priority"] \
                        and processes[i]["arrival"] < processes[selected]["arrival"]:
                    selected = i

        # Chưa có tiến trình nào đến -> CPU idle
        if selected == -1:
            current_time += 1
            continue

        # Chạy tiến trình được chọn trong 1 đơn vị thời gian
        remaining[selected] -= 1
        current_time += 1

        # Ghi vào Gantt chart (chỉ ghi khi đổi tiến trình)
        if not gantt or gantt[-1] != processes[selected]["pid"]:
            gantt.append(processes[selected]["pid"])

        # Tiến trình hoàn thành
        if remaining[selected] == 0:
            completion[selected] = current_time
            completed += 1

    # Tính Turnaround Time và Waiting Time
    turnaround = [completion[i] - processes[i]["arrival"] for i in range(n)]
    waiting = [turnaround[i] - processes[i]["burst"] for i in range(n)]

    return completion, turnaround, waiting, gantt
