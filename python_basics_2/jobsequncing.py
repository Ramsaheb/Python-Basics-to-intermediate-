def job_sequencing(deadlines, profits):
    n = len(profits)
    max_deadline = max(deadlines)
    result = [-1] * (max_deadline)
    total_profit = 0

    # Sort jobs in decreasing order of profit
    jobs = sorted(zip(profits, deadlines), key=lambda x: x[0], reverse=True)

    for profit, deadline in jobs:
        # Find a time slot from its deadline to 1
        for j in range(deadline - 1, -1, -1):
            if result[j] == -1:
                result[j] = profit
                total_profit += profit
                break

    return total_profit

# Taking input from the user for deadlines and profits
deadlines = list(map(int, input("Enter the deadlines separated by space: ").split()))
profits = list(map(int, input("Enter the profits separated by space: ").split()))

max_profit = job_sequencing(deadlines, profits)
print("Maximum profit:", max_profit)
