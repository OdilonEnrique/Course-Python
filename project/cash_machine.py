class Bank_account:
    def __init__(self, balance = 0):
        self.__balance = balance
        self.__file = "project/files/transactions.txt"

    def deposit(self, amount):
        self.__balance += amount

        try:
            with open(self.__file, "a") as file:
                file.write(f"deposito (+),  {amount}\n")
        except:
            print("Algo deu errado em abrir o arquivo!")
            pass

        print(f"Depósito de R${amount} realizado!")        

account = Bank_account()
waiting_menu = False # Flag

while True:
    if waiting_menu == True:
        input("\nPressione Enter para seguir...")

    # print("\033[H\033[J") #Terminal clear
    print("\033c", end="") # terminal clear
    waiting_menu = True

    print('''
=== Automed Teller Machine ===
    
    [1] Ver Extrato
    [2] Fazer o depósito
    [3] Fazer saque
    [4] Sair
==============================
''')

    option = input("\bEscolha uma opção:")
    print("")

    if option == "1":
        print("extratro")
    elif option == "2":
        amount = float(input("Digite o valor para depositar:"))
        account.deposit(amount)
    elif option == "3":
        print("saque")
    elif option == "4":
        print("Programa encerrado!\n")
        break
    else:
        print("Opção inválida")

