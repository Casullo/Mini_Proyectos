def fibonacci(n):
x = [0,1]
if n<=0:
return[]
    elif n==1:
    return[0]
         elif n==2:
        return[0,1]
        else:
            for i in range(n-2):
                x.append(x[-1]+x[-2])
                return x
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))


# solucion por indices:
#  def fibo(n):
# fibo_list = [0,1]
# if n == 0:
# return []
# elif n == 1:
# return [0]
# else:
# for i in range(1,n-1):
# siguiente = fibo_list[i-1] + fibo_list[i]
# fibo_list.append(siguiente)
# return fibo_list

# print(fibo(0))
# print(fibo(1))
# print(fibo(2))
# print(fibo(3))
# print(fibo(4))