import subprocess
import datetime
import os

def log(msg):
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{now}] {msg}")

def rodar_comando(cmd, check=True):
    log(f"Executando: {cmd}")
    subprocess.run(cmd, shell=True, check=check)

def main():
    try:
        log("🚀 Iniciando automação de notícias...")

        # Etapa 1: Coletar notícias
        rodar_comando("python coletar_noticias.py")

        # Etapa 2: Gerar site com base no JSON
        rodar_comando("python gerar_site.py")

        # Etapa 3: Git add, commit e push
        rodar_comando("git add .")
        rodar_comando('git commit -m "🤖 Atualização automática de notícias" || echo "Sem mudanças para commit"')
        rodar_comando("git push")

        log("✅ Site atualizado com sucesso!")

    except Exception as e:
        log(f"❌ Erro na automação: {e}")

if __name__ == "__main__":
    main()
