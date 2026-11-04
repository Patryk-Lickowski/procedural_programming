def count_available(events, expiry_time):
    if not events:
        return 0

    expires = {}  # process_id -> time it expires

    for op, pid, t in sorted(events, key=lambda e: e[2]):
        if op == 0:
            expires[pid] = t + expiry_time
        elif op == 1:
            # only restart if the process exists and hasn't expired yet
            if pid in expires and t <= expires[pid]:
                expires[pid] = t + expiry_time

    end_time = max(e[2] for e in events)
    return sum(1 for exp in expires.values() if exp >= end_time)


events = [[0, 1, 1], [0, 2, 2], [1, 1, 3], [1, 2, 10]]
print(count_available(events, 5))                     # 0
print(count_available([[0, 1, 1], [1, 1, 4]], 5))     # 1
print(count_available([[0, 1, 1], [0, 2, 2]], 5))     # 2
print(count_available([[1, 1, 3]], 5))                # 0
