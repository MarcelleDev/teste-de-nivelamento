import zipfile

def compactar_csv(csv_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, arcname=csv_path.split("/")[-1])


