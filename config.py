
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

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
