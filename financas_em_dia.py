salario = float(input("Digite seu salário: \n"))
limite_do_cartao_de_credito = int(input("Digite seu saldo de crédito disponível pelo banco: \n"))
compras = 0
valores_gastos_no_mes = 0

print("O total de gastos até o momento está no valor de R${}".format(valores_gastos_no_mes))

while valores_gastos_no_mes <= salario:
    compras = float(input("Digite o valor da compra: \n"))
    valores_gastos_no_mes = valores_gastos_no_mes + compras
    print("\nO total de gastos está no valor de R${}".format(valores_gastos_no_mes))

    if valores_gastos_no_mes > salario:
        saldo_negativo = valores_gastos_no_mes - salario
        print("O valor gasto (R${}) ultrapassa seu salário de (R${}) em (R${})".format(valores_gastos_no_mes, salario, saldo_negativo))
        print("Você está com credito negativado em R${}".format(saldo_negativo))
