def is_prime(prime_list, number):
    for n in prime_list:
        quo, mod = divmod(number, n)

        if mod == 0:
            return False
        elif quo < n:
            return True

while True:
    prime_list = [2, 3, 5, 7]

    try:
        list_len = int(input('Informe o tamanho da lista de números primos que deseja gerar (Vazio para encerrar o programa): '))
    except Exception as e:
        assert type(e).__name__ 
        break

    i = prime_list[-1] + 1
    while len(prime_list) < list_len:
        if is_prime(prime_list, i):
            prime_list.append(i)

        i += 1

    print(f'Lista dos primeiros {list_len} números primos: {prime_list}')