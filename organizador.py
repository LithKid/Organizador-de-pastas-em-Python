import shutil
from pathlib import Path

def organizar_downloads():
    downloads = Path.home() / "Downloads"

    pastas = {
        "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
        "PDFs": [".pdf"],
        "Planilhas": [".xlsx", ".xls", ".csv"],
        "Codigos": [".py", ".js", ".html", ".css"],
        "Compactados": [".zip", ".rar"]
    }

    for pasta in pastas:
        (downloads / pasta).mkdir(exist_ok=True)

    for arquivo in downloads.iterdir():
        if arquivo.is_file():
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

if __name__ == "__main__":
    organizar_downloads()