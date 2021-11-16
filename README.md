# WikiScraper

Utilitário extrator de informações da versão em língua portuguesa da Wikipédia.

Projeto referente à disciplina Teoria da Computação em nível de mestrado acadêmico do Programa de Pós-Graduação em Informática (PPGI) da Universidade Federal da Paraíba.


## Integrantes

VICTOR JOSÉ DE SOUSA KOEHLER (20211023501)

DAVID PEREIRA GALVÃO JÚNIOR (20211023510)

---


## Instruções de Execução

`python Scrapper.py [--specials] [--full-links]`

onde:

 - --specials: A lista de links passa a incluir as páginas especiais da Wikipédia. Vide `special_pages.py` e https://pt.wikipedia.org/wiki/Wikipédia:Domínio

 - --full-links: Imprime os links completos


## Dependências

- Python 3


## Links testados

 - [https://pt.wikipedia.org/wiki/St._James's_Park]()
 - https://pt.wikipedia.org/wiki/ISO/IEC_646 <sup>[0]</sup>
 - https://pt.wikipedia.org/wiki/LCFSA
 - https://pt.wikipedia.org/wiki/Organização_das_Nações_Unidas
 - https://pt.wikipedia.org/wiki/Efeito_Peltier
 - https://pt.wikipedia.org/wiki/Investigação_operacional
 - [https://pt.wikipedia.org/wiki/Rio_de_Janeiro_(estado)]()
 - https://pt.wikipedia.org/wiki/COVID-19
 - https://pt.wikipedia.org/wiki/&
 - https://pt.wikipedia.org/wiki/Matemática

[0]: Surpreendentemente, a Wikipédia abusa das normas das URIs (RFC3986), fazendo uso de "/" sem estritamente implicar na separação semântica de segmentos nas URLs dos artigos.


# Referências:

*https://en.wikipedia.org/wiki/Wikipedia:Page_name*

*https://en.wikipedia.org/wiki/Category:Restricted_titles*

*https://en.wikipedia.org/wiki/Wikipedia:Naming_conventions_(technical_restrictions)*

*https://en.wikipedia.org/wiki/Template:Correct_title*

*https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Dom%C3%ADnio*

*https://m.mediawiki.org/wiki/Manual:%24wgLegalTitleChars*

*https://datatracker.ietf.org/doc/html/rfc3986#section-3.3*
