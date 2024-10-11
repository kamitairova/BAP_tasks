def fence(numbers, n):
    min_sum = float('inf')
    min_indices = []

    for i in range(len(numbers) - n + 1):
        subset = numbers[i:i+n]
        subset_sum = sum(subset)
        
        if subset_sum < min_sum:
            min_sum = subset_sum
            min_indices = list(range(i+1, i+n+1)) 

    return min_indices

numbers = [1, 2, 6, 1, 1, 7, 1]
n = 4
result = fence(numbers, n)
print(result)