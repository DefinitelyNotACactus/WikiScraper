import re
import requests

# Padrões
# URL de artigo
URL_PATTERN = '(https?://)?pt.wikipedia.org/wiki/\w+'
# Título do artigo
TITLE_PATTERN = '<title>(.*?)( – Wikipédia, a enciclopédia livre)</title>'
# Índice de um artigo
INDEX_PATTERN = '<li class="toclevel-\d+( tocsection-\d+)?"><a href="(#\w+)"><span class="tocnumber">(\d+\.?\d*)</span> <span class="toctext">(.*?)</span>'
# Link para outro artigo
LINK_PATTERN = '<a href="(/wiki/\w+)" title="(.*?)">'
# Imagem
IMAGE_PATTERN = '<a href="/wiki/Ficheiro:(.*?\.\w+)" class="image"( title="(.*?)")?>'
# Cores de texto
ENDC = '\033[0m'
BOLD = '\033[1m'
# Propriedades do artigo
code = None
index = None
links = None
images = None
title = None
# Opção selecionada pelo usuário
option = None
# Variáveis auxiliares
index_searched = False
links_searched = False
images_searched = False
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

# Função para obter os tópicos e imprimi-los
def get_topics(code):
    global index_searched
    if index_searched is False: # A função não foi chamada anteriormente
        index = re.findall(INDEX_PATTERN, code)
        index_searched = True
    if len(index) > 0: # O artigo contém um índice
        print('Lista de tópicos')
        print('==============================================')
        for i in index:
            if re.search("\d+\.?\d+", i[2]): print('    ', i[2], i[3]) # Subseção
            else: print(i[2], i[3])
    else: # Artigo não possui índice
        # Exemplo de página sem índice: https://pt.wikipedia.org/wiki/Djalma_Marques
        print('O artigo não possui índice.')

# Função para obter os links para outros artigos
def get_links(code):
    global links_searched
    if links_searched is False: # A função não foi chamada anteriormente
        links_all = re.findall(LINK_PATTERN, code)
        links = {link[0]: link[1] for link in links_all} # Uso de dicionário para evitar a exibição de duplicatas
        links_searched = True
    if len(links) > 0:
        print('Lista de links para outros artigos da Wikipédia citados pelo artigo %s' % (title))
        print('==============================================')
        for (link_title, link) in zip(links.values(), links.keys()): print('Título: %s \nLink: %s' % (link_title, link))
    else: # O artigo não cita nenhum outro artigo
        print('O artigo não possui links para outros artigos.')

# Obter os nomes dos arquivos de imagens
def get_images(code):
    global images_searched
    if images_searched is False: # A função não foi chamada anteriormente
        images_all = re.findall(IMAGE_PATTERN, code)
        images = {image[0]: image[2] if len(image) == 3 else 'Sem título' for image in images_all} # Uso de dicionário para evitar a exibição de duplicatas
        images_searched = True
    if len(images) > 0:
        print('Lista de imagens do artigo')
        print('==============================================')
        for (image, image_title) in zip(images.keys(), images.values()): print('Nome do arquivo: %s\nTítulo: %s' % (image, image_title))
    else:
        print('O artigo não contém imagens.')

def main():
    while True:
        link = input('%sInsira a URL do artigo a ser analisado\n%s' % (BOLD, ENDC))
        print('==============================================')
        if re.search(URL_PATTERN, link):
            print('A URL informada é válida, acessando o artigo...')
            code = requests.get(link, headers=HEADERS).text
            index_searched = False
            links_searched = False
            images_searched = False
            title = re.findall(TITLE_PATTERN, code)[0][0]
            print('Artigo acessado: %s' % (title))
            while True:
                print('==============================================')
                option = input('Opções:\n1 - Ver índice do artigo' +
                    '\n2 - Ver os links para outros artigos citados' +
                    '\n3 - Obter os nomes dos arquivos de imagens do artigo' +
                    '\nAlternativamente, insira qualquer coisa para procurar por outro artigo\n')
                if option == '1': get_topics(code)
                elif option == '2': get_links(code)
                elif option == '3': get_images(code)
                else: break
        else:
            print('A URL "%s" não é válida.' % (link))

if __name__ == '__main__':
    main()