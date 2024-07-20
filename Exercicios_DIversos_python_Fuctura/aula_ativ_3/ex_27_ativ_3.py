"""27.	Dado o dicionário curso = {"nome": "Python", "duração": "3 meses"}, como você pode acessar o valor associado à chave duração?"""
curso = {
    "nome": "Python",
    "duração": "3 meses"
    }
print(curso.get("duração"))
print(curso.values())