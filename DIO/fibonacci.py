n = int(input())
fib_string = ''
if n > 0 and n < 46:
    fib_list = [0]
    fib_string = '0'
    n = n - 1
    if n > 0:
        fib_list.append(1)
        fib_string += ' 1'
    for i in range(1, n, 1):
        x = fib_list[i] + fib_list[i-1]
        fib_list.append(x)
        i += 1
        fib_string += ' ' + str(x)

print(fib_string)
print(len(fib_string))
