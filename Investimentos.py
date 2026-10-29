# Para simular e/ou calcular Juros compostos:
print('='*25, "Simulador de Juros Compostos", '='*25) # Para melhor apresentação visual.
Capital_inicial = float(input("Valor inicial (em R$): ")) # Solicita ao usuário a quantia de dinheiro que deseja colocar.
Juros = float(input("Qual a porcentagem (em %) dos juros?: ")) # Pergunta ao usuário a % dos juros aplicada.
Tempo = int(input("Quanto tempo ficará a sua renda (em meses)?: ")) # Quanto o dinheiro vai ficar aplicado rendendo junto com os juros.
Resultado = Capital_inicial * (1 + Juros/100)**Tempo # Montante inicial multiplicado pelo Juros dividido por 100 (para ficar em decimal) + 1 pois vai ser acrescido
                                                     # ao montante, elevado pela quantia Tempo.

Lucro = Resultado - Capital_inicial # Lucro é a diferença do Resultado e do montante inicial
Porcentagem_ganhos = ((Resultado / Capital_inicial) - 1) * 100 # A porcentagem de ganhos é A divisão do Resultado pelo montante inicial
                                                               # e é -1 para tirar o número inteiro, e é multiplicado por 100 pois vai colocar em % (porCENTO, de 100).

Resultado = print(f"\nO montante final será de: {Resultado:.2f} R$.\n\nLucro - Seu lucro é de {Lucro:.2f} R$.\n\nPorcentagem(%)de ganhos - Sua porcentagem de ganhos foi: {Porcentagem_ganhos:.3f} %.")
