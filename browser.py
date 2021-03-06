import re
from typing import Union, Optional
import config
from engine import InterpreterEngine

class EngineBrowserCLI:
    def __init__(self, engine : Optional[Union[InterpreterEngine, str]] = None):
        self.filter_special_urls = config.FILTER_SPECIAL_URLS
        self.full_links = config.FULL_LINKS
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
            link = eof_input('%sInsira a URL do artigo a ser analisado\n%s' % (config.BOLD, config.ENDC))
            if link is None: return
            print('==============================================')
            if re.fullmatch(config.URL_PATTERN, link):
                print('A URL informada é válida, acessando o artigo...')
                self.navigate(link)
                while True:
                    print('==============================================')
                    print('Artigo acessado: %s' % (self.engine.title))
                    if self.article_exists() is False: 
                        print('%sERRO: O artigo não existe%s' % (config.BOLD, config.ENDC))
                        print('==============================================')
                        break
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

    # Função para determinar se o artigo que está sendo acessado existe
    def article_exists(self):
        return self.engine.article_exists()

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
        links = list(self.engine.get_links(filter_special_urls=self.filter_special_urls))
        if len(links) > 0:
            print('Lista de links para outros artigos da Wikipédia citados pelo artigo %s' % (self.engine.title))
            print('==============================================')
            for li, l in enumerate(links):
                print(' (%d) %s : %s' % (li, l['titulo'], l['full_link' if self.full_links else 'link']))
            
            print('Para visitar um dos links acima, insira o seu número correspondente.')
            print('Para retornar, pressione ENTER: ', end='')
            opt = input().strip()
            if opt.isdigit():
                self.navigate(links[int(opt)]['full_link'])
            print()
        
        else: # O artigo não cita nenhum outro artigo
            print('O artigo não possui links para outros artigos.')

    # Obter os nomes dos arquivos de imagens
    def get_images(self):
        images = list(self.engine.get_images())
        if len(images) > 0:
            print('Lista de imagens do artigo')
            print('==============================================')
            for im in images:
                print(' %s : %s' % (im['titulo'] or '*', im['full_link' if self.full_links else 'arquivo']))
        else:
            print('O artigo não contém imagens.')
