import re
import requests

# Padrões
url_pattern = '(https?://)?pt.wikipedia.org/wiki/\w+'
index_pattern = '<li class="toclevel-\d+( tocsection-\d+)?"><a href="(#\w+)"><span class="tocnumber">(\d+\.?\d*)</span> <span class="toctext">(.*?)</span>'
link_pattern = '<a href="(/wiki/\w+)" title="(.*?)">'
image_pattern = '<a href="/wiki/Ficheiro:(\w+.\w+)" class="image" title="(.*?)">'
# Propriedades do artigo
code = None
index = None
links = None
images = None
# Cores de texto
ENDC = '\033[0m'
BOLD = '\033[1m'

def main():
    while True:
        link = input('%sInsira a URL do artigo a ser analisado\n%s' % (BOLD, ENDC))
        print('A URL "%s" é válida.' % (link))
        print('==============================================')
        if re.search(url_pattern, link):
            code = requests.get(link).text
            # Obter os tópicos
            index = re.findall(index_pattern, code)
            if len(index) > 0: # O artigo contém um índice
                print('Lista de tópicos')
                print('==============================================')
                #print(index)
                for i in index:
                    if re.search("\d+\.?\d+", i[2]): print('    ', i[2], i[3]) # Subseção
                    else: print(i[2], i[3])
                print('==============================================')
            else: # Artigo não possui índice
                # Exemplo de página sem índice: https://pt.wikipedia.org/wiki/Djalma_Marques
                print('O artigo não possui índice.')
            # Obter os links para outros artigos
            links = re.findall(link_pattern, code)
            if len(links) > 0:
                print('Lista de links para outros artigos da Wikipedia citados')
                print('==============================================')
                for link in links: print('Título: %s \nLink: %s' % (link[1], link[0])) # TODO: Proibir a impressão de links duplicados
                print('==============================================')
            else: # O artigo não cita nenhum outro artigo
                print('O artigo não possui links para outros artigos.')
            # Obter os nomes dos arquivos de imagens
            images = re.findall(image_pattern, code)
            if len(images) > 0:
                print('Lista de imagens do artigo')
                print('==============================================')
                for image in images: print('Nome do arquivo: %s\nTítulo: %s' % (image[0], image[1]))
                #for image in images: print()
                print('==============================================')
            else:
                print('O artigo não contém imagens.')
        else:
            print('A URL "%s" não é válida.' % (link))

        leave = input('Deseja pesquisar por outro artigo? (1 para Sim / Qualquer outra coisa Não): ')
        if leave != '1':
            break

if __name__ == '__main__':
    main()