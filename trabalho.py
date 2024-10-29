class Pilha:
    def __init__(self, maximo):
        self.itens = []
        self.maximo = maximo

    def adicionar(self, item):
        if len(self.itens) < self.maximo:
            self.itens.append(item)
            print(f"Item '{item}' adicionado.")
        else:
            print("A pilha está cheia! Não é possível adicionar mais itens.")

    def remover(self):
        if len(self.itens) > 0:
            item = self.itens.pop()
            print(f"Item '{item}' removido.")
        else:
            print("A pilha está vazia! Não há nada para remover.")

    def mostrar_topo(self):
        if len(self.itens) > 0:
            print(f"Item no topo: '{self.itens[-1]}'")
        else:
            print("A pilha está vazia.")

def main():
    maximo = int(input("Tamanho máximo da pilha: "))
    pilha = Pilha(maximo)

    while True:
        print("\nEscolha uma ação:")
        print("1) Adicionar")
        print("2) Remover")
        print("3) Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            item = input("Item para adicionar: ")
            pilha.adicionar(item)
        elif opcao == '2':
            pilha.remover()
        elif opcao == '3':
            print("Encerrando... Topo da pilha:")
            pilha.mostrar_topo()
            break
        else:
            print("Opção inválida, tente de novo.")

if __name__ == "__main__":
    main()
