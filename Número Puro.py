def is_primo(n):
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

def rotacoes_primas(n):
    n_str = str(n)
    rotacoes = []
    for i in range(len(n_str)):
        rotated = int(n_str[i:] + n_str[:i])
        if not is_primo(rotated):
            return []
        rotacoes.append(rotated)
    return rotacoes

def contagem_numeros_circulares_primos(total):
    count = 0
    for num in range(2, total):
        if all(is_primo(rot) for rot in rotacoes_primas(num)):
            count += 1
    return count

total = 10000
numeros_circulares = contagem_numeros_circulares_primos(total)
print(f"A quantidade total de números circulares primos: {numeros_circulares}")
