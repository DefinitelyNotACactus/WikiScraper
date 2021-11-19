from sys import argv
from special_pages import special_prefixes

# https://en.wikipedia.org/wiki/Wikipedia:Page_name
# https://en.wikipedia.org/wiki/Category:Restricted_titles
# https://en.wikipedia.org/wiki/Wikipedia:Naming_conventions_(technical_restrictions)
# https://en.wikipedia.org/wiki/Template:Correct_title
# https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Dom%C3%ADnio
# https://m.mediawiki.org/wiki/Manual:%24wgLegalTitleChars
# https://datatracker.ietf.org/doc/html/rfc3986#section-3.3

# Se links que levam a páginas especiais devem ser impressas (ver special_pages.py)
FILTER_SPECIAL_URLS = not '--specials' in argv
# Se deve imprimir o endereço completo de links e imagens
FULL_LINKS = '--full-links' in argv

# Padrões
# SUBPATH genérico
URL_SUBPATH = '([\w!#@$&:=%,\*\'\-\+\.\(\)]+)'
# URL de artigo
URL_PATTERN_BASE = '(https?://)?pt\.wikipedia\.org/wiki/'
URL_PATTERN = URL_PATTERN_BASE+URL_SUBPATH
# URL de página especial
SPECIAL_URL_PATTERN = URL_PATTERN_BASE + '({}):'.format('|'.join(special_prefixes)) + URL_SUBPATH
# Container principal
CONTAINER_PATTERN = '<main id="content" class="mw-body" role="main">([\S\s]+?)</main>'
# Título do artigo
TITLE_PATTERN = '<title>(.*?)( – Wikipédia, a enciclopédia livre)?</title>'
# Índice de um artigo
INDEX_PATTERN = '<li class="toclevel-\d+( tocsection-\d+)?"><a href="#(.*?)"><span class="tocnumber">(\d+(\.\d+)*)</span> <span class="toctext">(.*?)(<sup>(.*?)</sup>)?</span>'
# Link para outro artigo
LINK_PATTERN = '<a href="/wiki/'+URL_SUBPATH+'"( class="mw-redirect")? title="(.*?)">'
# Prefixo de Links (em consonância com o padrão anterior)
LINK_PREFIX = 'https://pt.wikipedia.org/wiki/'
# Imagem
IMAGE_PATTERN = '<a href="/wiki/Ficheiro:'+URL_SUBPATH+'" class="image"( title="(.*?)")?>'
OUTER_IMAGE_PATTERN = '<img(.*?)>'
IMAGE_ALT_PATTERN = 'alt="(.*?)"'
IMAGE_SRC_PATTERN = 'src="//upload\.wikimedia\.org/wikipedia/commons/thumb/(.*?)/(.*?)/'+URL_SUBPATH+'/?(.*?)?"'
# Prefixo de Imagens (em consonância com o padrão anterior)
IMAGE_PREFIX = LINK_PREFIX + 'Ficheiro:'
# Artigo não existe
NO_ARTICLE = '<b>A Wikipédia não possui um artigo com este nome exato\.</b>'
# Cores de texto
ENDC = '\033[0m'
BOLD = '\033[1m'

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
