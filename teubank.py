contas = []
agencia = "0001"
conta_atual = 0
senha_padrao = 111
saldo = 0 
total_valor = 0
limite = 500
LIMITE_SAQUE = 3

def carregar_clientes():
      try:
            with open("clientes.txt", "r") as arquivo:
                  linhas = arquivo.readlines()
                  for linha in linhas:
                        dados = linha.strip().split(",")
                        if len(dados) == 9:
                              cliente = {
                                    "nome": dados[0],
                                    "idade": dados[1],
                                    "endereco": dados[2],
                                    "cpf": dados[3],
                                    "conta": int(dados[4]),
                                    "senha": int(dados[5]),
                                    "saldo": float(dados[6]),
                                    "extrato": dados[7].replace('|', '\n'),
                                    "limitesaq": int(dados[8])
                                    }
                              contas.append(cliente)
      except FileNotFoundError:
            pass
      
      try:
            with open("config.txt", "r") as config_file:
                  linhas = config_file.readlines()
                  conta_atual = int(linhas[0])
                  senha_padrao = int(linhas[1])
      except FileNotFoundError:
            conta_atual = 0
            senha_padrao = 111
      return conta_atual, senha_padrao
                  
def salvar_clientes():
      with open("clientes.txt", "w") as arquivo:
            for cliente in contas:
                  extrato = cliente['extrato'].replace('\n', '|')
                  arquivo.write(f"{cliente['nome']}, {cliente['idade']}, {cliente['endereco']}, {cliente['cpf']}, {cliente['conta']}, {cliente['senha']}, {cliente['saldo']}, {cliente['extrato']}, {cliente['limitesaq']}\n")

      with open("config.txt", "w") as config_file:
            config_file.write(f"{conta_atual}\n{senha_padrao}")
carregar_clientes()

def inicio_Banco():
      print("""
      [1] - Criar Conta
      [2] - Entrar
      [3] - Esqueci meu acesso
      [4] - Lista de clientes
      [5] - Encerrar
      
Escolha uma das opções: """)
      
def verificar_conta(conta):
      for cliente in contas:
            if cliente['conta'] == conta:
                  return True
      return False

def verificar_senha(senha):
      for cliente in contas:
            if cliente['senha'] == senha:
                  return True
      return False
      
def criar_conta():
      global conta_atual
      global senha_padrao
      
      nome = input("Qual o nome do cliente: ")
      idade = input("Idade do cliente: ")
      endereco = input("Endereço do cliente: ")
      
      cpf = input("CPF do cliente: ")
      cliente_existente = encontrar_cpf(cpf)
      if cliente_existente:
            print("CPF já cadastrado. Não é possível criar outra conta com o mesmo CPF.")
            return
      
      while True:
            conta_atual += 1
            if not verificar_conta(conta_atual):
                  break
            
      while True:
            senha_padrao += 1
            if not verificar_senha(senha_padrao):
                  break
                  
      conta = conta_atual
      senha = senha_padrao
      
      saldo = 0
      extrato = ""
      limitesaq = 0
      
      print(f"Cliente: {nome}\nIdade: {idade} anos\nEndereço: {endereco}\nCPF: {cpf}\nConta: {conta}\nSenha: {senha}\nSaldo: {saldo}\nExtrato: {extrato}\nLimite Diário Saque: {limitesaq}")
            
      cliente = {
            "nome": nome,
            "idade": idade,
            "endereco": endereco,
            "cpf": cpf,
            "conta": conta,
            "senha": senha,
            "saldo": saldo,
            "extrato": extrato,
            "limitesaq": limitesaq
      }
      contas.append(cliente)
carregar_clientes()

def buscar_cliente(nome, conta_procurada):
      for cliente in contas:
            if cliente["nome"] ==  nome and cliente["conta"] == conta_procurada:
                  return cliente
      return None

def realizar_transferencia(origem, destino, valor):
      cliente_origem = encontrar_cliente(origem)
      cliente_destino = encontrar_cliente(destino)
      
      if cliente_origem and cliente_destino:
            if valor > 0 and cliente_origem["saldo"] >= valor:
                  cliente_origem["saldo"] -= valor
                  cliente_destino["saldo"] += valor
                  extrato_origem = cliente_origem["extrato"]
                  destino = cliente_destino["nome"]
                  extrato_origem += f"Transferência realizada para conta {destino} no valor de R${valor}\n"
                  cliente_origem["extrato"] = extrato_origem
                  extrato_destino = cliente_destino["extrato"]
                  origem = cliente_origem["nome"]
                  extrato_destino += f"Transferência recebida da conta de {origem} no valor de R${valor}\n"
                  cliente_destino["extrato"] = extrato_destino
                  print("=" * 60)
                  print("Transferência realizada com sucesso!")
                  print("=" * 60)
            else:
                  print("=" * 60)
                  print("Valor inválido ou saldo insuficiente para realizar a transferência")
                  print("=" * 60)
      else:
            print("=" * 60)
            print("Conta não encontrada.")
            print("=" * 60)

def encontrar_cliente(conta_procurada):
      for cliente in contas:
            if cliente["conta"] == conta_procurada:
                  return cliente
      return None

def encontrar_cpf(cpf_procurado):
      for cliente in contas:
            if cliente["cpf"] == cpf_procurado:
                  return cliente
      return None

def buscar_dados_cliente(cliente):
      print(f"Nome: {cliente['nome']}")
      print(f"Conta: {cliente['conta']}")
      print(f"Senha: {cliente['senha']}")
                  
def entrar_conta():
      print("Para entrar na sua conta digite: ")
      print("Agência = 0001")
      conta_entra = int(input("Conta: "))
      senha = int(input("Senha: "))
      
      cliente = encontrar_cliente(conta_entra)
      if cliente and cliente["senha"] == senha:
            return cliente
      else:
            print("Conta ou senha inválida. Tente novamente.")
            return None

def menu_princ():
      print(
            """
      Selecione uma das opções abaixo:       
      [1] - Depositar
      [2] - Sacar
      [3] - Extrato Bancário
      [4] - Transferência
      [0] - Sair
      """)
carregar_clientes()
      
while True:
      inicio_Banco()
      escolha = input()

      print("="*30)
      
      if escolha == "1": # criar conta
            print("Bem-vindo ao Teu Bank. Vamos criar sua conta\n")
            criar_conta()
            
      elif escolha == "2": # entrar na conta
            cliente_logado = entrar_conta()
            if cliente_logado:
                  "\n"
                  "\n"
                  print("=" * 60)
                  print("Acesso autorizado")
                  print("=" * 60)
                  while True:
                        "\n"
                        "\n"
                        print('Bem-vindo(a),', cliente_logado["nome"].title())
                        print(f"Saldo atual R$:", cliente_logado['saldo'])
                        menu_princ()
                        opcao = input()
                              
                        if opcao == "1":
                              print("Qual o valor a ser depositado")
                              valor = float(input("R$:"))
                              if valor > 0:
                                    cliente_logado["saldo"] += valor
                                    extrato = cliente_logado["extrato"]
                                    extrato += f"Depósito no valor de R${valor}\n"
                                    cliente_logado["extrato"] = extrato
                                    print("=" * 50)
                                    print(f"Depósito efetuado com sucesso. Saldo R$:{cliente_logado['saldo']}")
                              else:
                                    print("=" * 50)
                                    print("Operação inválida. Tente novamente!")
                                    print("=" * 50)
                              
                        elif opcao == "2":
                              if cliente_logado['limitesaq'] < LIMITE_SAQUE:
                                    rest_saque = LIMITE_SAQUE - cliente_logado['limitesaq']
                                    print(f"Você tem {LIMITE_SAQUE} saques diários. Restam {rest_saque} saques")
                              else:
                                    print("=" * 50)
                                    print ("Você utilizou todos os saques diários disponíveis!")
                                    print("=" * 50)
                                    continue
                              print("Digite o valor a ser sacado")
                              valor = float(input("R$: "))
                              if valor > cliente_logado["saldo"] and cliente_logado['limitesaq'] < 3:
                                    print("=" * 65)
                                    print("Valor de saque maior que o limite disponível. Tente novamente!")
                                    print("=" * 65)
                              elif valor <= cliente_logado["saldo"] and valor <= 500:
                                    extrato = cliente_logado["extrato"]
                                    extrato += f"Saque no valor de R${valor}\n"
                                    cliente_logado["extrato"] = extrato                                    
                                    cliente_logado["saldo"] -= valor
                                    print("=" * 60)
                                    print(f"Saque efetuado com sucesso. Saldo atual na conta: {cliente_logado['saldo']}")
                                    print("=" * 60)
                                    cliente_logado['limitesaq'] += 1 
                                    for cliente in contas:
                                          cliente["conta"] == contas
                              else:
                                    print("=" * 50)
                                    print("Você só pode sacar R$500 por vez.")
                                    print("=" * 50)
                                    print("-" * 50)
                                    print(f"Seu saldo atual é R$ {cliente_logado['saldo']}")
                              
                        elif opcao == "3":
                              print("=" * 50)
                              print("Extrato Bancário | Ultimas movimentações:\n")
                              print(cliente_logado["extrato"])
                              print("=" * 50)
                              
                        elif opcao == "4":
                              print("Digite o valor a ser transferido?")
                              valor = float(input("R$:"))
                              conta_destino = int(input("Digite o número da conta a receber a transferência: "))
                              realizar_transferencia(cliente_logado["conta"], conta_destino, valor)
                                                                  
                        elif opcao == "0":
                              print("Obrigado por usar o TeuBank.")
                              break
                        else:
                              print("=" * 50)
                              print("Opção inválida, tente novamente!")
                              print("=" * 50)
   
      elif escolha == "3": #esqueci o acesso
            rec_nome = input("Digite seu nome: ")
            rec_conta = int(input("Digite sua conta: "))
            cliente_recuperado = buscar_cliente(rec_nome, rec_conta)
            if cliente_recuperado:
                  buscar_dados_cliente(cliente_recuperado)
            else:
                  print("Cliente não encontrado.")
                        
      if escolha == "4": # listar clientes
            print("Apenas os administradores tem acesso. Entre com sua conta Admin")
            user_adm = input("Entre com o login: ")
            passw_adm = input("Entre com a senha: ")
            if user_adm == "admin" and passw_adm == "0":
                  for cliente in contas:
                        print(cliente)
            else:
                  print("Usuário inválido e/ou não autorizado.")
                  inicio_Banco()
      if escolha == "5": # encerrar banco
            salvar_clientes()
            break