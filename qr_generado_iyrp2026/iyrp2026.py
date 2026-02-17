import qrcode
import os

# Crear carpeta si no existe
os.makedirs("qr_generado_barcelo", exist_ok=True)

base_url = "https://open.spotify.com/playlist/0Ig1hRYlEExJgrCTuzYICy"

# Generar el código QR
img = qrcode.make(base_url)

# Guardar la imagen dentro de la carpeta
img.save("qr_generado_barcelo/qr_barcelo.png")

print("QR generado correctamente.")
