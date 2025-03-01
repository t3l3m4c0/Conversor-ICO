import os
from PIL import Image

# Definir rutas
carpeta_input = "C:/conversor_ico/input/"
carpeta_output = "C:/conversor_ico/output/"

# Verificar si la carpeta de salida existe, si no, crearla
if not os.path.exists(carpeta_output):
    os.makedirs(carpeta_output)

# Obtener lista de imágenes en la carpeta input
imagenes = [f for f in os.listdir(carpeta_input) if f.lower().endswith((".png", ".bmp", ".jpg", ".jpeg"))]

# Verificar si hay imágenes disponibles
if not imagenes:
    print("No hay imágenes en la carpeta input.")
    exit()

# Mostrar menú al usuario
print("Imágenes disponibles en input:")
for idx, img in enumerate(imagenes, 1):
    print(f"{idx}. {img}")

print("0. Convertir TODAS las imágenes\n")

# Pedir al usuario una opción
opcion = input("Selecciona el número de la imagen a convertir o 0 para todas: ")

# Si elige 0, convierte todas las imágenes
if opcion == "0":
    archivos_a_convertir = imagenes
    print("Convirtiendo todas las imágenes...\n")
else:
    try:
        idx = int(opcion) - 1
        if 0 <= idx < len(imagenes):
            archivos_a_convertir = [imagenes[idx]]
        else:
            print("Opción no válida.")
            exit()
    except ValueError:
        print("Entrada no válida.")
        exit()

# Convertir las imágenes seleccionadas a .ico
for archivo in archivos_a_convertir:
    ruta_entrada = os.path.join(carpeta_input, archivo)
    nombre_base = os.path.splitext(archivo)[0]  # Nombre sin extensión
    ruta_salida = os.path.join(carpeta_output, f"{nombre_base}.ico")

    # Cargar la imagen y convertirla en .ico con múltiples tamaños
    imagen = Image.open(ruta_entrada)
    imagen = imagen.convert("RGBA")  # Asegurar compatibilidad
    tamaños_ico = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    imagen.save(ruta_salida, format="ICO", sizes=tamaños_ico)


    print(f"Convertido: {archivo} -> {ruta_salida}")

print("¡Conversión completada!")
