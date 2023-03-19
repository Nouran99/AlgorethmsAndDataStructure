import time

start_without =time.time()
def fib_without (num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fib_without(num - 1) + fib_without(num - 2)
end_without =time.time()
print (end_without-start_without)

start_DP =time.time()
def fib_DP(num):
    fib = []
    for i in range (0,num+1):
        fib.append(-1)
    fib[0] = 0
    fib[1] = 1
    for i in range (2,num+1):
        fib[i]=fib[i-2]+fib[i-1]
    return fib[i]
end_DP =time.time()
print (end_DP-start_DP)


print(fib_without(15))
print(fib_DP(15))
