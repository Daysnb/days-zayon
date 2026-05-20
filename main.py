from conta import Conta
conta = Conta()

while true:
  print() #so pra pular uma linhazinha :) #genial
  print("1. Depositar")
  print("2. Sacar")
  print("3. Ver saldo")
  print("4, Ver rendimento")

opcao = input("Escolha uma opção: ")

if opcao == "1":
  valor = float(input("Valor do deposito; "))
  conta.deposita(valor)

elif opcao == "2":
  valor = float(input("Valor do saque: ")
  conta.saca(valor)

elif opcao == "3":
  print("Saldo:", conta.saldo)

elif opcao == "4":
  print("Rendimento:", conta.calcula_rendimento()) #É calcula_rendimento msm :) #W

else:
  ("Opção invalida, por favor tente novamente.")


#belo codigo zigoto
