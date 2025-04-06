import time
import subprocess
from datetime import datetime

def rodar_automatizacao():
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] 🚀 Iniciando automação de notícias...")

    comandos = [
        "python coletar_noticias.py",
        "python gerar_site.py",
        "git add .",
        'git commit -m "🤖 Atualização automática de notícias" || echo "Sem mudanças para commit"',
        "git push"
    ]

    for cmd in comandos:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Executando: {cmd}")
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ❌ Erro na automação: {e}")
            break

while True:
    rodar_automatizacao()
    print("⏳ Aguardando 1 hora para a próxima execução...")
    time.sleep(3600)  # Aguarda 1 hora
