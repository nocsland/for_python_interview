def get_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)


number = int(input())
get_factorial(number)
