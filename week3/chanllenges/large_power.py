def power_check(base, exponent):
    '''check if base raised to exponent is greater than 5000'''
    result = base ** exponent


    if result>5000:
        return True
    else:
        return False
    
        # ask for user input
base= int(input('enter base'))
exponent= int(input('enter exponent'))


print(power_check(base, exponent))