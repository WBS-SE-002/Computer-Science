numbers = [3, 5, 7, 2, 8]  # Example list
largest = numbers[0]  # Step 3

for num in numbers[1:]:  # Step 4
    print(num)
    if num > largest:  # Step 4a
        largest = num  # Step 4a i

print("The largest number is:", largest)


text = "Hello World!"

for char in text:
    print(char)
