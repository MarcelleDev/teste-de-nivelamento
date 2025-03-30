import os
import zipfile

zip_filename = "dados/anexos.zip"

with zipfile.ZipFile(zip_filename, "w") as zipf:
    for pdf in os.listdir("dados"):
        if pdf.endswith(".pdf"):
            zipf.write(os.path.join("dados", pdf), pdf)

print(f"Arquivos compactados em {zip_filename}")

