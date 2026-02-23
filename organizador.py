import os
import shutil
from pathlib import Path

# Pequeno organizador de arquivos para a pasta "Downloads".
# - Define categorias em `pastas` (nome da pasta -> lista de extensões)
# - Cria as pastas de destino dentro de Downloads
# - Percorre os arquivos em Downloads e move para a pasta correspondente

# Caminho da pasta Downloads do usuário
downloads = Path.home() / "Downloads"  # Nota: variável com nome 'dowload' (possível typo)

# Mapeamento de pastas para extensões de arquivo
pastas = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "PDFs": [".pdf"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "compactados": [".zip", ".rar"]
}
for pasta in pastas:
        (downloads / pasta).mkdir(exist_ok=True)  # Cria pasta se não existir   

# Criar subpastas em Downloads para cada categoria.
# ATENÇÃO: a linha abaixo usa `downloads` (variável NÃO definida no script).
# Para executar o script sem erro, troque `downloads` por `dowload` ou renomeie a variável.


# Percorre itens em `dowload` e processa apenas arquivos (ignora diretórios).
for arquivo in downloads.iterdir():
    if arquivo.is_file():
        # Para cada arquivo, verifica a extensão e move para a primeira
        # pasta cujo conjunto de extensões contenha a extensão do arquivo.
        for pasta, extensoes in pastas.items():
            if arquivo.suffix.lower() in extensoes:
                destino = downloads / pasta / arquivo.name
                shutil.move(str(arquivo), str(destino))
                print(f"Movendo {arquivo.name} para {pasta}")               
destino = downloads / pasta / arquivo.name

contador =1 
while destino.exists():
    novo_nome = f"{arquivo.stem}_{contador}{arquivo.suffix}"
    destino = downloads / pasta / novo_nome
    contador += 1
    shutil.move(str(arquivo), str(destino))
    print(f"Movendo {arquivo.name}movido para {pasta}")

# Sugestões rápidas:
# - Corrigir o nome da variável `dowload` para `downloads` (ou vice-versa)
#   para evitar NameError ao criar pastas.
# - Tratar possíveis exceções (permissões, arquivos em uso) com try/except
# - Adicionar opção de dry-run para testar sem mover arquivos.