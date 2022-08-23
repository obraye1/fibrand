def fibo(n):
    print(1)
    counter = 1
    old_num = 0
    new_num = 1
    sum_fib = 1
    fj = []
    while counter < n:
        fib = old_num + new_num
        
        print(fib)

        if counter < n:
            old_num = new_num
            new_num = fib
            sum_fib = sum_fib + fib
            counter = counter + 1

    print(f'The sum of the first 50 value of a Fibonacci series {sum_fib}')



fibo(50)
