def is_prime(n):
    eh_primo = True
    if n != 2 and n % 2 == 0:
        eh_primo = False
    else:
        i = 3
        while i < n // 2 and eh_primo:
            if n % i == 0:
                eh_primo = False
            i += 2

    return eh_primo


"""
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
"""
print(is_prime(9))
