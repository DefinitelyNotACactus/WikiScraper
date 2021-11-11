import re
from typing import Union, Optional
from config import *
from engine import InterpreterEngine

class EngineBrowserCLI:
    def __init__(self, engine : Optional[Union[InterpreterEngine, str]] = None):
        if engine is not None:
            self.engine = self.navigate(engine)

    def navigate(self, url) -> InterpreterEngine:
        self.engine = InterpreterEngine(url) if isinstance(url, str) else url
        return self.engine
    
    def main_loop(self):
        def eof_input(*args, **kwargs):
            try:
                return input(*args, **kwargs)
            except EOFError:
                return None
        while True:
            link = eof_input('%sInsira a URL do artigo a ser analisado\n%s' % (BOLD, ENDC))
            if link is None: return
            print('==============================================')
            if re.search(URL_PATTERN, link):
                print('A URL informada é válida, acessando o artigo...')
                self.navigate(link)
                while True:
                    print('Artigo acessado: %s' % (self.engine.title))
                    print('==============================================')
                    option = eof_input('Opções:\n1 - Ver índices do artigo' +
                        '\n2 - Ver os links para outros artigos citados' +
                        '\n3 - Obter os nomes dos arquivos de imagens do artigo' +
                    '\nAlternativamente, insira qualquer coisa para procurar por outro artigo\n')
                    if option == '1': self.get_topics()
                    elif option == '2': self.get_links()
                    elif option == '3': self.get_images()
                    elif option is None: return
                    else: break
            else:
                print('A URL "%s" não é válida.' % (link))

    # Função para obter os tópicos e imprimi-los
    def get_topics(self):
        topics = list(self.engine.get_topics())
        if len(topics) > 0:
            print('Lista de tópicos')
            print('==============================================')
            for t in topics:
                print('    '*t['nivel'], t['numeração'], t['titulo'])
        else:
            # Exemplo de página sem índice: https://pt.wikipedia.org/wiki/Djalma_Marques
            print('O artigo não possui índice.')

    # Função para obter os links para outros artigos
    def get_links(self):
        links = list(self.engine.get_links())
        if len(links) > 0:
            print('Lista de links para outros artigos da Wikipédia citados pelo artigo %s' % (self.engine.title))
            print('==============================================')
            for li, l in enumerate(links):
                print(' (%d) %s : %s' % (li, l['titulo'], l['link']))
            
            print('Para visitar um dos links acima, insira o seu número correspondente.')
            print('Para retornar, pressione ENTER: ', end='')
            opt = input().strip()
            if opt.isdigit():
                self.navigate('https://pt.wikipedia.org'+links[int(opt)]['link'])
        
        else: # O artigo não cita nenhum outro artigo
            print('O artigo não possui links para outros artigos.')

    # Obter os nomes dos arquivos de imagens
    def get_images(self):
        images = list(self.engine.get_images())
        if len(images) > 0:
            print('Lista de imagens do artigo')
            print('==============================================')
            for im in images:
                print(' %s : %s' % (im['titulo'] or '*', im['arquivo']))
        else:
            print('O artigo não contém imagens.')
