print("Bem-vindo(a) ao Quiz da SNCT!")
pontos = 0

print("1. Quem é considerada a primeira programadora da história?")
print("a) Marie Curie")
print("b) Ada Lovelace")
print("c) Grace Hopper")

resposta = input("Digite a letra da resposta correta: ")

if resposta.lower() == "b":
  print("Você acertou! Ada Lovelace escreveu o primeiro algoritmo no século XIX.")
  pontos = pontos + 1
else:
  print("Que pena, a resposta correta era 'b) Ada Lovelace'.")

print(f"Fim de jogo! Você fez {pontos} ponto(s).")