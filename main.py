# aqui vai importar bibliotecas para manipular os arquivos
import os
# essa função askdirectory permite executar a abertura de um pop up para selecionar uma pasta no pc
from tkinter.filedialog import askdirectory

# aqui ele abre um pop up para selecionar uma pasta desejada
caminho = askdirectory(title="Selecione uma pasta")

# aqui vai listar os aquivos presentes dentro da pasta selecionada
lista_arquivos = os.listdir(caminho)

# nessa parte vai direcionar quais arquivos vão receber suas classificações, pra quais locais esse arquivos vão
locais = {
  "imagens": [".png", ".jpg"],
  "planilhas": [".xlsx"],
  "pdfs": [".pdf"],
  "csvs": [".csv"],
}

# agora vai percorrer cada arquivo dentro da lista e extrair a extensão do arquivo
for arquivo in lista_arquivos:

# essa função splitext vai extrair as extensões, isso seria por exemplo isso aqui: # 01. Arquivo.pdf e pra fazer o split precisa passar pra ele o nome do arquivo
  nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

#  basicamente funciona assim: pra cada pasta dentro dos meu locais esse "for" vai verificar se a extensão está dentro da lista
# dentro do "if" será verificado se não existe a pasta a partir do comando: "os.path.exists" 
# ele vai criar a pasta destinada para aquele tipo de arquivo com o comando "mkdir" e joga esse arquivo para uma nova pasta criada com o comando "rename" e assim será criado uma pasta nova transformando o nome do antigo para o novo.
  for pasta in locais:
      if extensao in locais[pasta]:
          if not os.path.exists(f"{caminho}/{pasta}"):
             os.mkdir(f"{caminho}/{pasta}")
          os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
# tudo isso vai movimentar nossos arquivos e enviar para as pastas destinadas