import os
from datetime import datetime
from git import Repo

# Ruta absoluta del repo dentro del contenedor
repo_path = "/app"
repo = Repo(repo_path)

# Ruta relativa al archivo Excel dentro del repo
archivo_excel = "3.Subir_datos/1.Base_capital/data/Data_final.xlsx"

fecha_hoy = datetime.now().strftime("%Y-%m-%d")

if repo.is_dirty(path=archivo_excel, untracked_files=True):
    repo.git.add(archivo_excel)
    repo.index.commit(f"Subida automática del archivo a carpeta {fecha_hoy}")

    token = "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"
    usuario = "AnaliticaDatosLagobo"
    repo_name = "Agente_simuldor_libranza"

    url_con_token = f"https://{usuario}:{token}@github.com/{usuario}/{repo_name}.git"

    repo.git.push(url_con_token, "HEAD:main")

    print("🚀 ¡Archivo subido correctamente a GitHub!")
else:
    print("⚠️ El archivo no ha cambiado. No se hizo commit ni push.")
