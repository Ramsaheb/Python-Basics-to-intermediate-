def knapsack(cap, weight, profit, n):
    if n == 0 or cap == 0:
        return 0
    elif weight[n - 1] > cap:
        return knapsack(cap, weight, profit, n - 1)
    else:
        return max(profit[n - 1] + knapsack(cap - weight[n - 1], weight, profit, n - 1),
                   knapsack(cap, weight, profit, n - 1))
    
print('Enter the profits : ')
profit = list(map(int, input().split()))
print('Enter the weight : ')
weight = list(map(int, input().split()))
cap = int(input('Enter the capacity : '))
n = len(weight)
print(knapsack(cap, weight, profit, n))
