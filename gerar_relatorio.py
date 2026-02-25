import json
from funcoes import carregar_cadastros
from openpyxl import Workbook

def gerar_relatorio():
    cadastros = carregar_cadastros()

    print(f'dados carregados: {cadastros}')

    if not cadastros:
        print("|Nenhum cadastro encontrado para gerar o relatório!|\n")
        return
    
    workbook = Workbook()
    planilha = workbook.active
    planilha.title = "Cadastros"
    planilha.append(["nome", "idade","email"])

    for pessoa in cadastros:
        planilha.append([pessoa.get("nome"), pessoa.get("idade"), pessoa.get("email")])
    workbook.save("relatorio_cadastros.xlsx")
    print("\n|Relatório gerado com sucesso!|\n")

if __name__ == "__main__":
    gerar_relatorio()