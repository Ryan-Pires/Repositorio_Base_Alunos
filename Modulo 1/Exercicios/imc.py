nome = input("Digite o nome do paciente: ")
peso = float(input("Digite o peso do paciente: "))
altura = float(input("Digite a altura do paciente: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Acima do peso")
elif imc < 34.9:
    print("Obesidade Grau I")
elif imc < 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III(mórbida)")

print(f"O IMC do paciente {nome} é {imc:.2f}")