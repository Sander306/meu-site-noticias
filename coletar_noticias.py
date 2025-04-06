import feedparser
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

FEEDS = {
    "G1": "https://g1.globo.com/rss/g1/",
    "UOL": "https://rss.uol.com.br/feed/noticias.xml",
    "R7": "https://www.r7.com/rss/"
}

def limpar_html(soup):
    for tag in soup(["script", "style", "aside", "footer", "noscript"]):
        tag.decompose()
    return soup

def extrair_conteudo(link):
    try:
        r = requests.get(link, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        soup = limpar_html(soup)
        texto = " ".join([p.get_text(strip=True) for p in soup.find_all("p")])
        titulo = soup.find("title").get_text(strip=True)
        imagem = soup.find("img")
        imagem_url = imagem["src"] if imagem and "src" in imagem.attrs else ""
        return titulo, texto, imagem_url
    except:
        return "", "", ""

def coletar():
    noticias = []
    for fonte, url in FEEDS.items():
        feed = feedparser.parse(url)
        for item in feed.entries[:10]:
            titulo, texto, imagem = extrair_conteudo(item.link)
            if not titulo or not texto:
                continue
            noticias.append({
                "fonte": fonte,
                "titulo": titulo,
                "resumo": item.get("summary", "")[:200],
                "imagem": imagem,
                "conteudo": texto,
                "link_original": item.link,
                "publicado_em": item.get("published", str(datetime.now()))
            })
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    coletar()

import feedparser
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

FEEDS = {
    "G1": "https://g1.globo.com/rss/g1/",
    "UOL": "https://rss.uol.com.br/feed/noticias.xml",
    "R7": "https://www.r7.com/rss/"
}

def limpar_html(soup):
    for tag in soup(["script", "style", "aside", "footer", "noscript"]):
        tag.decompose()
    return soup

def extrair_conteudo(link):
    try:
        r = requests.get(link, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        soup = limpar_html(soup)
        texto = " ".join([p.get_text(strip=True) for p in soup.find_all("p")])
        titulo = soup.find("title").get_text(strip=True)
        imagem = soup.find("img")
        imagem_url = imagem["src"] if imagem and "src" in imagem.attrs else ""
        return titulo, texto, imagem_url
    except:
        return "", "", ""

def coletar():
    noticias = []
    for fonte, url in FEEDS.items():
        feed = feedparser.parse(url)
        for item in feed.entries[:10]:
            titulo, texto, imagem = extrair_conteudo(item.link)
            if not titulo or not texto:
                continue
            noticias.append({
                "fonte": fonte,
                "titulo": titulo,
                "resumo": item.get("summary", "")[:200],
                "imagem": imagem,
                "conteudo": texto,
                "link_original": item.link,
                "publicado_em": item.get("published", str(datetime.now()))
            })
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    coletar()
 
