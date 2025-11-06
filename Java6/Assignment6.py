def optimizeInventory(shelfCapacity, batches):
    n = len(batches)
    dp = [[0] * (shelfCapacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        size = batches[i - 1]['size']
        priority = batches[i - 1]['priority']
        for w in range(shelfCapacity + 1):
            if size <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - size] + priority)
            else:
                dp[i][w] = dp[i - 1][w]

    w = shelfCapacity
    acceptedBatches = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            acceptedBatches.append(batches[i - 1]['id'])
            w -= batches[i - 1]['size']

    acceptedBatches.reverse()

    return {
        "maxPriority": dp[n][shelfCapacity],
        "acceptedBatches": acceptedBatches
    }


capacity1 = 50
batches1 = [
    {"id": "B001", "size": 10, "priority": 60},
    {"id": "B002", "size": 20, "priority": 100},
    {"id": "B003", "size": 30, "priority": 120},
    {"id": "B004", "size": 15, "priority": 80}
]

print(optimizeInventory(capacity1, batches1))
