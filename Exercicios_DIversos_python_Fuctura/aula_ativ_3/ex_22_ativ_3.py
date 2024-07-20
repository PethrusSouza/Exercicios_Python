"""22.	Dado o dicionário contato = {"nome": "Alice", "telefone": "1234-5678"}, como você pode remover a chave telefone?"""
contato = {
    "nome": "Alice", 
    "telefone": "1234-5678"
    }
del contato["telefone"]
print(contato)