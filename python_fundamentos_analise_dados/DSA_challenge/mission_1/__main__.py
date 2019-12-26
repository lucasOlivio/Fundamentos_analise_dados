from collections import Counter 

def has_unique_chars(string):
    if string is None:
        return False
    
    if len(string) == 0:
        return True

    res = Counter(string).most_common(1)

    if res[0][1] > 1:
        return False
    else:
        return True

while True:

    validation = has_unique_chars(input('Informe uma string para avaliação (Vazio para fechar o programa):'))

    print(validation)