import json

cadastros = []

def salvar_cadastros():
    with open("cadastros.json", "w") as arquivo:
        json.dump(cadastros, arquivo, indent=4)

def carregar_cadastros():
    global cadastros
    try:
        with open("cadastros.json", "r") as arquivo:
            cadastros = json.load(arquivo)
            return cadastros
        
    except FileNotFoundError:
        cadastros = []
        return []

def cadastrar_pessoa():

    while True:
        nome = input("Nome: ").title()

        if nome.replace(" ", "").isalpha():
            break
        else:
            print("|O nome deve possuir apenas letras|")

    while True:
        entrada = input("Idade: ")
        idade_validada = validar_idade(entrada)

        if idade_validada is not None:
            idade = idade_validada
            break
        else:
            print("|Digite uma idade válida!|")

    while True:
        email = input("Email: ")
        if validar_email(email):
            break
        else:
            print("|Email inválido!|")

    pessoa = {
        "Nome": nome,
        "Idade": idade,
        "Email": email
    }

    cadastros.append(pessoa)
    salvar_cadastros()
    print("\n|Cadastro realizado com sucesso!|\n")

def remover_cadastro():
    if not cadastros:
        print("|A lista está vazia!|\n")
        return

    listar_cadastros()

    try:
        escolha = int(input('Escolha o número do cadastro a ser removido: '))

        if 1 <= escolha <= len(cadastros):
                removido = cadastros.pop(escolha - 1)
                salvar_cadastros()
                print(f"\n|Cadastro de {removido['nome']} removido com sucesso!|\n")
        else:
                print('\n|Número inválido!|\n')

    except ValueError:
        print('\n|Digite um número válido!|')   


def listar_cadastros():
    if not cadastros:
        print('\n|A lista está vazia!|\n')
    else:
        print("\n|Lista de pessoas cadastradas|")
        print('=' * 50)
        for i , pessoa in enumerate(cadastros, start = 1):
            print(f"{i}. Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Email: {pessoa['email']}")
        print('=' * 50)
        print()

def editar_cadastro():
    if not cadastros:
        print("\n|Não há cadastros para editar!|\n")
        return

    listar_cadastros()

    try:
        escolha = int(input("Escolha o número do cadastro a ser editado: "))

        if not (1 <= escolha <= len(cadastros)):
            print("\n|Número inválido!|\n")
            return

        pessoa = cadastros[escolha - 1]

        print("\n|Pressione ENTER para manter o valor atual|")

        while True:
            novo_nome = input(f"Nome({pessoa['nome']}): ").title()
            if not novo_nome:
                break        

            if novo_nome.replace(" ", "").isalpha():
                pessoa["nome"] = novo_nome
                break
            else:
                print("|O nome deve possuir apenas letras|")


        while True:
            nova_idade = input(f"Idade ({pessoa['idade']}): ")

            if not nova_idade:
                break

            idade_validada = validar_idade(nova_idade)

            if idade_validada is not None:
                pessoa["idade"] = idade_validada
                break
            else:
                print("|Digite uma idade válida!|")

        while True:
            novo_email = input(f"Email ({pessoa['email']}): ")

            if not novo_email:
                break

            if validar_email(novo_email):
                pessoa["email"] = novo_email
                break
            else:
                print("|Email inválido!|")

        salvar_cadastros()
        print("\n|Cadastro atualizado com sucesso!|\n")

    except ValueError:
        print("\n|Digite um número válido!|\n")

def validar_idade(valor):
    try:
        idade = int(valor)
        if 1 <= idade <= 120:
            return idade
        else:
            return None
    except ValueError:
        return None

def validar_email(email):
    return "@" in email and "." in email