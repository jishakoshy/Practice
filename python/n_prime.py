# return n prime numbers -> 2,3,5,7,11,13,17,19,23,29

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True  

N = 100
for num in range(1, N + 1):
    if is_prime(num): 
        print(num, end=" ")

