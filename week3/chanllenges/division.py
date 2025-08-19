def divisible_by_10(num):
    remainder = num % 10

    if remainder == 0:
        return True
    else:
        return False
    
print(divisible_by_10(10))