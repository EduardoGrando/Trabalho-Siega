class Pilha:
    def __init__(self):
        self.dados = []

    def inserir(self, letra):
        self.dados.append(letra)

    def retirar(self):
        return self.dados.pop()

    def vazia(self):
        return len(self.dados) == 0

def verificar_palindromo(texto):
    pilha = Pilha()
    for letra in texto:
        pilha.inserir(letra)

    texto_invertido = ''.join([pilha.retirar() for _ in texto])

    return texto == texto_invertido

def main():
    texto = input("Digite uma palavra: ").upper()
    if verificar_palindromo(texto):
        print(f"'{texto}' é um palíndromo.")
    else:
        print(f"'{texto}' não é um palíndromo.")

if __name__ == "__main__":
    main()
