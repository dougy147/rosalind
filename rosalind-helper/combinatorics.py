def factorial(n):
    m=1
    while n > 0:
        m*=n
        n-=1
    return m

def combinations(k,n): return factorial(n) // (factorial(n-k) * factorial(k))
def arrangements(k,n): return factorial(n) // factorial(n-k)
