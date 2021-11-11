import re
import requests
from config import *

class InterpreterEngine:
    def __init__(self, url, code=None):
        self.url = url
        self.code = code or requests.get(url, headers=HEADERS).text
        self.title = re.findall(TITLE_PATTERN, self.code)[0][0]

    # Função para obter os tópicos e imprimi-los
    def get_topics(self):
        index = re.findall(INDEX_PATTERN, self.code)
        for i in index:
            yield { 'titulo': i[3], 'numeração': i[2], 'nivel': 1 if re.search("\d+\.?\d+", i[2]) else 0 }

    # Função para obter os links para outros artigos
    def get_links(self):
        links_all = re.findall(LINK_PATTERN, self.code)
        links = {link[0]: link[1] for link in links_all} # Uso de dicionário para evitar a exibição de duplicatas
        for (link_title, link) in zip(links.values(), links.keys()):
            yield { 'titulo': link_title, 'link': link }

    # Obter os nomes dos arquivos de imagens
    def get_images(self):
        images_all = re.findall(IMAGE_PATTERN, self.code)
        images = {image[0]: image[2] if len(image) == 3 else 'Sem titulo' for image in images_all} # Uso de dicionário para evitar a exibição de duplicatas
        for (image, image_title) in zip(images.keys(), images.values()):
            yield { 'titulo': image_title, 'arquivo': image }

