def contar_decrescente(n: int) -> list[int]:
    if n < 0:
        raise ValueError("Forneça um inteiro >= 0")
    return list(range(n, -1, -1))


if __name__ == "__main__":
    valor = int(input("Digite um inteiro >= 0: "))
    print(contar_decrescente(valor))
