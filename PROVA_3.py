def numero_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def rotacao(n):
    n_str = str(n)
    numeros_rotacionados = [n]
    for i in range(1, len(n_str)):
        rotated = int(n_str[i:] + n_str[:i])
        numeros_rotacionados.append(rotated)
        
    return numeros_rotacionados


def contagem(total):
    contagem = 0
    for num in range(2, total):
        if all(numero_primo(rot) for rot in rotacao(num)):
            contagem += 1
    return contagem

  


total = 1000000
numeros_circulares = contagem(total)
print(f"A quantidade total dos números circulares : {numeros_circulares}")
