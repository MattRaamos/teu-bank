print("""
      Bem-Vindo(a) ao TeuBank
      """)

menu = """
      Selecione uma das opções abaixo:       
      [1] - Depositar
      [2] - Sacar
      [3] - Extrato Bancário
      [0] - Sair
      
      """
      
saldo = 0 
limite = 500
extrato_banc = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
          print("Qual o valor a ser depositado")
          valor = float(input("R$:"))
          if valor > 0:
                saldo += valor
                extrato_banc = extrato_banc + f"Depósito no valor de R${valor}\n"
                print("=" * 50)
                print(f"Depósito efetuado com sucesso. Saldo R$:{saldo}")
                print("=" * 50)
          else:
                print("=" * 50)
                print("Operação inválida. Tente novamente!")
                print("=" * 50)
          
    elif opcao == "2":
          if numero_saque < LIMITE_SAQUE:
                rest_saque = LIMITE_SAQUE - numero_saque
                print(f"Você tem {LIMITE_SAQUE} saques diários. Restam {rest_saque} saques")
          else:
                print("=" * 50)
                print ("Você utilizou todos os saques diários disponíveis!")
                print("=" * 50)
                continue
          print("Qual o valor a ser sacado")
          valor = float(input("R$:"))
          if valor > saldo and numero_saque < 3:
                print("=" * 65)
                print("Valor de saque maior que o limite disponível. Tente novamente!")
                print("=" * 65)
          if valor <= saldo and valor <= 500:
                extrato_banc = extrato_banc + f"Saque no valor de R${valor}\n"
                novo_saldo = saldo - valor
                saldo = novo_saldo
                print("=" * 60)
                print(f"Saque efetuado com sucesso. Saldo atual na conta: {saldo}")
                print("=" * 60)
                numero_saque = numero_saque + 1
          elif valor > 500:
                print("=" * 50)
                print("Você só pode sacar R$500 por vez.")
                print("=" * 50)
                print("-" * 50)
          print(f"Seu saldo atual é R$ {saldo}")

       
    elif opcao == "3":
          print("=" * 50)
          print("Extrato Bancário | Ultimas movimentações:\n")
          print(extrato_banc)
          print("=" * 50)
      
          
    elif opcao == "0":
          print("Obrigado por usar o TeuBank.")
          break
    else:
          print("=" * 50)
          print("Opção inválida, tente novamente!")
          print("=" * 50)

    
         




    