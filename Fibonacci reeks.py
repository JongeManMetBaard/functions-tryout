def fib(num):

    a = 0
    b = 1

    if num == 1:
        return a

    else:

        d = "0 1 "
        for i in range(2,num):
            c = a + b
            a = b
            b = c
            d += str(c) + " "
        return d



num = int(input("Which Fibonacci number do you want to see?")) 
print(fib(num))