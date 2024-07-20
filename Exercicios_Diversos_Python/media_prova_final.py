"""Em uma determinada faculdade, dado que um estudante não atingiu a média 7,0, este precisará fazer uma
prova final. A nota mínima na avaliação final para que este estudante seja aprovado é dada pela seguinte
fórmula: NF = (50 - Média x 6) ÷ 4. Assim, com base nessa informação desenvolva um programa que
solicite três notas e caso esteja abaixo da média, calcule qual a nota mínima que o estudante precisa
tirar na avaliação final para passar."""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media_aritmetrica = (n1 + n2 + n3) / 3
if media_aritmetrica < 7:
    nota_final = (50 - media_aritmetrica * 6) / 4
    print(f"sua media foi {media_aritmetrica:.1f}")
    print(f"Voce não atingia a nota necessária para ser aprovado, e fará uma PROVA FINAL precisando tirar {nota_final}")
else:
    print(f"SUA MEDIA FOI {media_aritmetrica:.1f} PARABENS VOCÊ FOI APROVADO")    