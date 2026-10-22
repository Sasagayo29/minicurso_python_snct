# =====================================================================
# MINICURSO: Mulheres na Tecnologia (23ª SNCT - IFTM)
# Script: Quiz Expandido
# Objetivo: Treinar listas, laços de repetição (for) e condicionais (if/else)
# =====================================================================

print("=" * 40)
print(" 👩‍💻 QUIZ: PIONEIRAS DA TECNOLOGIA 👩‍💻 ")
print("=" * 40)
print("Vamos testar seus conhecimentos sobre as mulheres que construíram a história da TI!\n")

pontuacao = 0

# Lista de perguntas, opções e as respostas corretas
# Usamos uma estrutura de dicionário para organizar melhor os dados
perguntas = [
    {
        "pergunta": "1. Quem escreveu o primeiro algoritmo da história no século XIX?",
        "opcoes": "a) Marie Curie \nb) Ada Lovelace \nc) Grace Hopper",
        "resposta_correta": "b"
    },
    {
        "pergunta": "2. Qual cientista da computação cunhou o termo 'Bug' e ajudou a criar a linguagem COBOL?",
        "opcoes": "a) Grace Hopper \nb) Margaret Hamilton \nc) Katherine Johnson",
        "resposta_correta": "a"
    },
    {
        "pergunta": "3. Quem foi a diretora de engenharia de software responsável pelo código do Projeto Apollo 11 (que levou o homem à Lua)?",
        "opcoes": "a) Ada Lovelace \nb) Hedy Lamarr \nc) Margaret Hamilton",
        "resposta_correta": "c"
    },
    {
        "pergunta": "4. Além de atriz de Hollywood, quem inventou a tecnologia de salto de frequência que originou o Wi-Fi e o Bluetooth?",
        "opcoes": "a) Hedy Lamarr \nb) Radia Perlman \nc) Katie Bouman",
        "resposta_correta": "a"
    }
]

# O laço 'for' vai passar por cada pergunta da nossa lista automaticamente
for item in perguntas:
    print(item["pergunta"])
    print(item["opcoes"])
    
    # Pegamos a resposta e transformamos em minúscula (lower) para evitar erros
    resposta = input("Digite a letra correta (a, b ou c): ").lower()
    
    if resposta == item["resposta_correta"]:
        print("✅ Correto! Muito bem.\n")
        pontuacao += 1 # Adiciona 1 ponto
    else:
        print(f"❌ Incorreto. A resposta certa era '{item['resposta_correta']}'.\n")

# Calculando o resultado final
print("=" * 40)
print(f"🎉 FIM DO JOGO! Sua pontuação final foi: {pontuacao} de {len(perguntas)}")

if pontuacao == 4:
    print("Incrível! Você é uma verdadeira especialista em história da tecnologia!")
elif pontuacao >= 2:
    print("Mandou bem! Conhece bastante sobre o nosso legado.")
else:
    print("Obrigado por jogar! O importante é sempre aprender coisas novas.")
print("=" * 40)