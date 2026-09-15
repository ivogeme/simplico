# simplico.py
import os

def interpretar_comando(linha, estado):
    linha = linha.strip()
    if linha.startswith("CRIAR SISTEMA"):
        nome = linha.replace("CRIAR SISTEMA", "").strip('" ')
        print(f"🔧 Sistema criado: {nome}")
        estado["sistema"] = nome
    elif linha.startswith("TELA:"):
        campos = linha.replace("TELA:", "").strip().split(",")
        campos = [c.strip() for c in campos]
        estado["campos"] = campos
        estado["dados"] = {}
        for campo in campos:
            valor = input(f"{campo}: ")
            estado["dados"][campo] = valor
    elif linha.startswith("ARMAZENAR EM"):
        arquivo = linha.replace("ARMAZENAR EM", "").strip('" ')
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(f"{estado['dados']}\n")
        print(f"📁 Dados armazenados em: {arquivo}")
    elif linha.startswith("IMPRIMIR"):
        msg = linha.replace("IMPRIMIR", "").strip('" ')
        print(f"🖨️ {msg}")
    elif linha == "ENCERRAR":
        print("✅ Sistema encerrado com sucesso.")
        exit(0)
    else:
        print(f"⚠️ Comando desconhecido: {linha}")

def interpretar_arquivo(caminho_arquivo):
    estado = {}
    if not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado.")
        return
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    for linha in linhas:
        interpretar_comando(linha, estado)

if __name__ == "__main__":
    arquivo = input("Digite o nome do script (.txt): ").strip()
    interpretar_arquivo(arquivo)