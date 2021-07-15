# generators 



def genfibonnaci(n):
    a=1
    b=5 
    for i in range(n):
        yield a
        a,b = b,a+b


for num in genfibonnaci(10):
    print(num)

