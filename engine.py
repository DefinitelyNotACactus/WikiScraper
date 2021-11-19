import re
import requests
from sys import stderr
from urllib.parse import unquote
from config import *

class InterpreterEngine:
    def __init__(self, url, code=None):
        self.url = url
        if isinstance(url, str) and not url.startswith('http'):
            url = 'https://' + url.lstrip(':/')
        self.full_code = code or requests.get(url, headers=HEADERS).text
        extr = re.search(CONTAINER_PATTERN, self.full_code)
        if extr: self.code = extr.group(0)
        else:
            print('ALERTA: Container não identificado.', extr, file=stderr) # Como resultado, um número
            self.code = self.full_code # excessivo de links e imagens podem acabar sendo capturados
        self.title = re.findall(TITLE_PATTERN, self.full_code)[0][0]

    # Função para determinar se o artigo que está sendo acessado existe
    # Quando o artigo não existe, o link leva à uma página com uma mensagem padrão
    def article_exists(self):
        return len(re.findall(NO_ARTICLE, self.code)) == 0

    # Função para obter os tópicos e imprimi-los
    def get_topics(self):
        index = re.findall(INDEX_PATTERN, self.code)
        for i in index:
            yield { 'titulo': i[4], 'numeração': i[2], 'nivel': i[2].count('.') }

    def is_special_url(self, url):
        return re.fullmatch(SPECIAL_URL_PATTERN, url)

    # Função para obter os links para outros artigos
    def get_links(self, filter_special_urls=False):
        links_all = re.findall(LINK_PATTERN, self.code)
        links = {link[0]: link[2] for link in links_all}
        for (link, link_title) in links.items():
            if filter_special_urls and self.is_special_url(LINK_PREFIX + link):
                continue
            yield { 'titulo': unquote(link_title), 'link': link, 'full_link': LINK_PREFIX + link }

    # Obter os nomes dos arquivos de imagens
    def get_images(self):
        def inner_extract(img_tag):
            image_link = re.findall(IMAGE_SRC_PATTERN, img_tag)[0]
            image_title = re.findall(IMAGE_ALT_PATTERN, img_tag)[0]
            image_file = image_link.split('/')[-1]
            return { 'titulo': unquote(image_title), 'arquivo': image_file, 'full_link': image_link, 'set_link': image_link }
        def outer_extract(a):
            i = inner_extract(a[3])
            l = IMAGE_PREFIX + a[0]
            return { 'titulo': a[2] or i['titulo'], 'arquivo': a[0] or i['arquivo'], 'full_link': l or i['set_link'], 'set_link': i['set_link'] }
        images_all =  [outer_extract(i) for i in re.findall(IMAGE_PATTERN, self.code)]
        images_all += [inner_extract(i) for i in re.findall(OUTER_IMAGE_PATTERN, self.code)]
        images_set = set() # Uso de set para evitar a exibição de duplicatas
        for img in images_all:
            if img['set_link'] in images_set:
                continue
            images_set.add(img['set_link'])
            yield img

