def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

print("Enter the numbers with space separated values:")
data = list(map(int, input().split(' ')))
mean_value = calculate_mean(data)
print("Mean:", mean_value)