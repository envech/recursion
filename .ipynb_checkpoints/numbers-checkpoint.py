def sum_of_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_numbers(n - 1)

result = sum_of_numbers(538)
print(result)