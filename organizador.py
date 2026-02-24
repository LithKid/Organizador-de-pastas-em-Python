import shutil
import sys
from pathlib import Path

def organizar_downloads():

    # Define a pasta alvo
    if len(sys.argv) > 1:
        downloads = Path(sys.argv[1])
    else:
        downloads = Path.home() / "Downloads"

    print("Pasta selecionada:", downloads)

    # Verifica se a pasta existe
    if not downloads.exists():
        print(f"A pasta '{downloads}' não existe.")
        return

    pastas = {
        "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
        "PDFs": [".pdf"],
        "Planilhas": [".xlsx", ".xls", ".csv"],
        "Codigos": [".py", ".js", ".html", ".css"],
        "Compactados": [".zip", ".rar"],
        "executaveis": [".exe", ".msi"],
        "documentos": [".docx", ".doc", ".txt"]
    }

    # Cria as pastas se não existirem
    for pasta in pastas:
        (downloads / pasta).mkdir(exist_ok=True)

    arquivos_encontrados = False

    # Percorre os arquivos
    for arquivo in downloads.iterdir():
        if arquivo.is_file():
            arquivos_encontrados = True
            print("Arquivo encontrado:", arquivo.name)

            for pasta, extensoes in pastas.items():
                if arquivo.suffix.lower() in extensoes:
                    destino = downloads / pasta / arquivo.name

                    contador = 1
                    while destino.exists():
                        novo_nome = f"{arquivo.stem}_{contador}{arquivo.suffix}"
                        destino = downloads / pasta / novo_nome
                        contador += 1

                    shutil.move(str(arquivo), str(destino))
                    print(f"{arquivo.name} movido para {pasta}")
                    break

    if not arquivos_encontrados:
        print("Nenhum arquivo encontrado na pasta.")

if __name__ == "__main__":
    organizar_downloads()