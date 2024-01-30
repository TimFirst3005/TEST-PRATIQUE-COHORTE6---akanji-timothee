

def ComputeMultiplesSum(n):
    if n >= 0 and n<1000:
        res = 0
        for i in range(n):
            if n%3==0 or n%5==0 or n%7==0:
                res += i
    return res
