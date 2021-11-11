import re
import requests
from sys import stderr
from urllib.parse import unquote
from config import *

class InterpreterEngine:
    def __init__(self, url, code=None):
        self.url = url
        self.full_code = code or requests.get(url, headers=HEADERS).text
        extr = re.search(CONTAINER_PATTERN, self.full_code)
        if extr: self.code = extr.group(0)
        else:
            print('ALERTA: Container não identificado.', extr, file=stderr) # Como resultado, um número
            self.code = self.full_code # excessivo de links e imagens podem acabar sendo capturados
        self.title = re.findall(TITLE_PATTERN, self.full_code)[0][0]

    # Função para obter os tópicos e imprimi-los
    def get_topics(self):
        index = re.findall(INDEX_PATTERN, self.code)
        for i in index:
            yield { 'titulo': i[4], 'numeração': i[2], 'nivel': i[2].count('.') }

    # Função para obter os links para outros artigos
    def get_links(self):
        links_all = re.findall(LINK_PATTERN, self.code)
        links = {link[0]: link[2] for link in links_all}
        for (link, link_title) in links.items():
            yield { 'titulo': unquote(link_title), 'link': link, 'full_link': LINK_PREFIX_PATTERN + link }

    # Obter os nomes dos arquivos de imagens
    def get_images(self):
        images_all = re.findall(IMAGE_PATTERN, self.code)
        images = {image[0]: image[2] if len(image) == 3 else 'Sem titulo' for image in images_all} # Uso de dicionário para evitar a exibição de duplicatas
        for (image, image_title) in images.items():
            yield { 'titulo': image_title, 'arquivo': image, 'full_link': IMAGE_PREFIX_PATTERN + image }

