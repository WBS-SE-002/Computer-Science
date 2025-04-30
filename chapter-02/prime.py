user_input = int(input("What number do you want to check? "))

is_prime = True

for i in range(2, user_input):
    if (user_input % i) == 0:
        is_prime = False
        break


print(is_prime)