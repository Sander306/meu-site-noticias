import json
import os
from slugify import slugify

# Instale: pip install python-slugify

HTML_HEAD = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{titulo}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{resumo}">
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 20px;
      max-width: 800px;
    }}
    .card {{
      border: 1px solid #ddd;
      padding: 15px;
      margin-bottom: 20px;
      border-radius: 8px;
    }}
    img {{
      max-width: 100%;
      height: auto;
    }}
    a {{
      text-decoration: none;
      color: blue;
    }}
  </style>
</head>
<body>
"""

HTML_FOOTER = """
</body>
</html>
"""

def gerar_paginas():
    with open("noticias.json", encoding="utf-8") as f:
        noticias = json.load(f)

    os.makedirs("noticias", exist_ok=True)

    index_cards = ""

    for i, noticia in enumerate(noticias):
        slug = slugify(noticia['titulo'])[:50]
        nome_arquivo = f"noticia-{i+1}-{slug}.html"
        caminho = os.path.join("noticias", nome_arquivo)

        with open(caminho, "w", encoding="utf-8") as f_out:
            conteudo = f"""
            {HTML_HEAD.format(titulo=noticia['titulo'], resumo=noticia['resumo'])}
            <div class="card">
                <h1>{noticia['titulo']}</h1>
                <p><em>Fonte: {noticia['fonte']} - {noticia['publicado_em']}</em></p>
                <img src="{noticia['imagem']}" alt="imagem" />
                <p>{noticia['conteudo'].replace('\n', '<br>')}</p>
                <p><a href="{noticia['link_original']}" target="_blank">Leia na fonte original</a></p>
            </div>
            {HTML_FOOTER}
            """
            f_out.write(conteudo)

        # Criar card para index
        index_cards += f"""
        <div class="card">
            <h2><a href="noticias/{nome_arquivo}">{noticia['titulo']}</a></h2>
            <p>{noticia['resumo']}</p>
        </div>
        """

    # Criar index.html
    with open("index.html", "w", encoding="utf-8") as f_index:
        f_index.write(f"{HTML_HEAD.format(titulo='Notícias', resumo='Resumo de notícias')}")
        f_index.write(index_cards)
        f_index.write(HTML_FOOTER)

if __name__ == "__main__":
    gerar_paginas()
