def fibonacci(n):
    sequence = [0, 1]
    if n <= 1:
        return "Please use a bigger number"
    if n <= 2:
        return sequence

    for i in range(0, n):
        x = sequence[i]
        y = sequence[i+1]
        z = x + y
        sequence.append(z)
    # sequence.append(sequence[x-1] + sequence[x-2])

    return sequence


# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(10))
