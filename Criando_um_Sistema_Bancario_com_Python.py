menu  = """

    [d] = Depositar
    [s] = Sacar
    [e] = Extrato
    [q] = Sair
=> """
saldo = 0;
limite = 500;
extrato  ="" ;
numero_saques = 0;
LIMITE_SAQUES = 3 ;

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o Valor do deposito:"));

        if valor > 0:
            saldo += valor ;
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else: 
            print("Operação Invalida, Valor informado e invalido");
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "));
        execedeu_saldo = valor > saldo;
        execedeu_limite = valor > limite ;
        execedeu_saques  = numero_saques >= LIMITE_SAQUES ;

        if execedeu_saldo:
            print("Operação falhou: Saldo insuficiente!");
        elif execedeu_limite:
            print("Operação invalida: Limite excedito!");
        elif execedeu_saques:
            print("Operação invalida: Limite de saques Diario excedito!")
        elif valor > 0:
            saldo += valor;
            extrato += f"Saque : R$ {valor: .2f} \n";
            numero_saques += 1;
        else:
            print("Operação Invalida: O valor informado e invalido");
    
    elif opcao == "e":
        print("############ EXTRATO ############");
        print("Não foram Realizadas Movimentações." if not extrato else extrato);
        print(f"\n Saldo: R${saldo: .2f}");
        print("#################################");

    elif opcao == "q":
        break;
    
    else:
        print("Operação invalida, Selecione a operação desejada: ");

