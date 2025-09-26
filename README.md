Organizador de Arquivos

Este projeto é um organizador automático de arquivos que separa documentos de uma pasta em subpastas de acordo com sua extensão.
Ele utiliza Python e a biblioteca Tkinter para permitir a seleção da pasta por meio de uma janela pop-up.

🔧 Funcionalidades

Seleciona uma pasta através de uma interface gráfica.

Lê todos os arquivos dentro da pasta escolhida.

Organiza os arquivos em subpastas de acordo com o tipo:

Imagens → .png, .jpg

Planilhas → .xlsx

PDFs → .pdf

CSVs → .csv

Cria automaticamente as pastas caso ainda não existam.

📂 Estrutura criada

Após a execução, dentro da pasta escolhida, será criada a seguinte estrutura (dependendo dos arquivos presentes):

📁 PastaSelecionada
 ┣ 📁 imagens
 ┃ ┗ arquivo.png
 ┣ 📁 planilhas
 ┃ ┗ arquivo.xlsx
 ┣ 📁 pdfs
 ┃ ┗ arquivo.pdf
 ┣ 📁 csvs
 ┃ ┗ arquivo.csv

🚀 Como executar
1. Clonar este repositório
git clone https://github.com/Victorvkt/organizador-de-arquivos
cd organizador-arquivos

2. Criar ambiente virtual (opcional, mas recomendado)
python -m venv venv


Ativar:

Windows → venv\Scripts\activate

Linux/Mac → source venv/bin/activate

3. Executar o script
python main.py

📦 Dependências

Python 3.7+

Bibliotecas nativas (não é necessário instalar nada extra):

os

tkinter

🖼️ Exemplo de uso

Ao rodar o programa, uma janela será exibida pedindo para você selecionar a pasta desejada.

O script irá automaticamente organizar os arquivos em subpastas de acordo com suas extensões.

💡 Possíveis melhorias

Adicionar suporte a mais tipos de arquivos (vídeos, documentos do Word, etc).

Criar um instalador com PyInstaller para rodar sem precisar do Python.

Permitir personalizar extensões e pastas via arquivo de configuração.
