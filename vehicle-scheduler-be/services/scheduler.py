def knapsack(tasks, capacity):

    n = len(tasks)

    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):

        duration = tasks[i-1]["Duration"]
        impact = tasks[i-1]["Impact"]

        for w in range(capacity+1):

            if duration <= w:

                dp[i][w] = max(
                    impact + dp[i-1][w-duration],
                    dp[i-1][w]
                )

            else:

                dp[i][w] = dp[i-1][w]

    selected = []

    w = capacity

    for i in range(n,0,-1):

        if dp[i][w] != dp[i-1][w]:

            selected.append(tasks[i-1])

            w -= tasks[i-1]["Duration"]

    selected.reverse()

    return {
        "TotalImpact": dp[n][capacity],
        "SelectedTasks": selected
    }