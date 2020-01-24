def pow(a, b):
    print(a**b)
    
def smart_pow(func):
    
    def inner(a, b):
        if a<b:
            a, b = b, a
        return func(a, b)
    
    return inner

pow = smart_pow(pow)

pow(2, 3)