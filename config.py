
# Padrões
# SUBPATH genérico
URL_SUBPATH = '([\w!@$&:=%,\*\'\-\+\.\(\)]+)'
# URL de artigo
URL_PATTERN = '(https?://)?pt\.wikipedia\.org/wiki/'+URL_SUBPATH
# Container principal
CONTAINER_PATTERN = '<main id="content" class="mw-body" role="main">([\S\s]+?)</main>'
# Título do artigo
TITLE_PATTERN = '<title>(.*?)( – Wikipédia, a enciclopédia livre)</title>'
# Índice de um artigo
INDEX_PATTERN = '<li class="toclevel-\d+( tocsection-\d+)?"><a href="#(.*?)"><span class="tocnumber">(\d+(\.\d+)*)</span> <span class="toctext">(.*?)(<sup>(.*?)</sup>)?</span>'
# Link para outro artigo
LINK_PATTERN = '<a href="/wiki/'+URL_SUBPATH+'"( class="mw-redirect")? title="(.*?)">'
# Prefixo de Links (em consonância com o padrão anterior)
LINK_PREFIX_PATTERN = 'https://pt.wikipedia.org/wiki/'
# Imagem
IMAGE_PATTERN = '<a href="/wiki/Ficheiro:'+URL_SUBPATH+'" class="image"( title="(.*?)")?>'
# Prefixo de Imagens (em consonância com o padrão anterior)
IMAGE_PREFIX_PATTERN = LINK_PREFIX_PATTERN + 'Ficheiro:'
# Cores de texto
ENDC = '\033[0m'
BOLD = '\033[1m'

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
