saldo = 0.0
limite_saque = 500.0
extrato = []
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!") 
    else:
        print("Erro: O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo, extrato, numero_saques
    if numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("Erro: Limite diário de saques de saques atingido (3 saques por dia).") 
    elif valor > limite_saque:
        print(f"Erro: O valor máximo por saque é R${limite_saque:.2f}.")
    elif valor > saldo:
        print("Erro: Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R${valor:.2f}")
        numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

def exibir_extrato():
    global saldo, extrato
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo atual: R${saldo:.2f}")

print("==============================")

def menu():
    while True:
        print("\n======== MENU ========")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        print("====================")

        opcao = input("Escolha uma opção")
        
        if opcao == "1":
            try:
                valor = float(input("Digite o valor do depósito: R$"))
                depositar(valor)
            except ValueError:
                print("Erro: Valor inválido.")
        elif opcao == "2":
            try:
                valor = float(input("Digite o valor do saque: R$"))
                sacar(valor)
            except ValueError:
                print("Erro: Valor inválido.")
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    menu()                                     





