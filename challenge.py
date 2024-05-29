def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = int(input("Digite o número de termos da sequência de Fibonacci: "))
print(fibonacci(n))

n = 8

while n > 0:
    array = [1,1]
    f = array[-1] + array[-2]
    array.append(f)
    n -=1

print(array)