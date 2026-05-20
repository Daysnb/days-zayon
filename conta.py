class Conta:
  def __init(self):
    self.saldo = 0

  def saca(self, valor):
    self.saldo -= valor 

  def deposita(self, valor):
    self.saldo += valor 

  def calcula_rendimento(self):
    return self.saldo * 0.1

conta = conta()

conta.deposita(100)

print(conta.saldo)

print(conta.calcula_rendimento())



#codigo mt bom man parabens :)

#obrigado =>
