import time

def contagem_regressiva(n):
    if n == 0:
        return
    else:
        print(n,'...')
        time.sleep(1)
        contagem_regressiva(n - 1)

class TorreDeControle:
    def __init__(self):
        self.pilha_decolagens = []
        self.fila_pousos = []
    
    def adicionar_decolagem(self, aviao):
        self.pilha_decolagens.append(aviao)
        print(f'Avião {aviao} adicionado para a decolagem.')
    
    def adicionar_pouso(self, aviao):
        self.fila_pousos.append(aviao)
        print(f'Avião {aviao} adicionado para pouso.')
    
    def realizar_decolagem(self):
        if self.pilha_decolagens:
            aviao = self.pilha_decolagens.pop()
            print(f'Iniciando a contagem regressiva para a decolagem do {aviao}.')
            contagem_regressiva(5)
            print(f'Decolagem concluida do {aviao}.')
        else:
            print("Nenhum avião disponível para decolar.")
    
    def realizar_pouso(self):
        if self.fila_pousos:
            aviao = self.fila_pousos.pop(0)
            print(f"Iniciando contagem regressiva para pouso do {aviao}:")
            contagem_regressiva(5)
            print(f"Pouso concluído do {aviao}!")
        else:
            print("Nenhum avião disponível para pousar.")
    
    def exibir_status(self):
        print(f"Total de aviões para decolagem: {len(self.pilha_decolagens)}")
        print(f"Total de aviões para pouso: {len(self.fila_pousos)}")
        if self.pilha_decolagens:
            print("Aviões na fila de decolagem:", ", ".join(self.pilha_decolagens))
        if self.fila_pousos:
            print("Aviões na fila de pouso:", ", ".join(self.fila_pousos))

def menu():
    torre = TorreDeControle()
    while True:
        print("\n1. Adicionar avião para decolar")
        print("2. Adicionar avião para pousar")
        print("3. Realizar decolagem")
        print("4. Realizar pouso")
        print("5. Exibir status do aeroporto")
        print("6. Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            aviao = input("Digite o identificador do avião (Ex: Avião 101): ")
            torre.adicionar_decolagem(aviao)
        elif escolha == '2':
            aviao = input("Digite o identificador do avião (Ex: Avião 202): ")
            torre.adicionar_pouso(aviao)
        elif escolha == '3':
            torre.realizar_decolagem()
        elif escolha == '4':
            torre.realizar_pouso()
        elif escolha == '5':
            torre.exibir_status()
        elif escolha == '6':
            print("Saindo do sistema... ")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()