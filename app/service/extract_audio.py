import subprocess


def extract_audio(input_file: str):
    print(f'Extrayendo audio del archivo {input_file}')
    
    # Nombre del archivo de salida .mp3
    output_file = input_file.rsplit('.', 1)[0] + '.mp3' 

    command = [
        'ffmpeg',
        '-i', input_file,
        '-vn',                      # Sin video
        '-ar', '44100',            # Tasa de muestreo
        '-ac', '2',                # Canal estéreo
        '-b:a', '128k',            # Tasa de bits
        '-threads', 'auto',        # Usa hilos
        '-y',                       # Sobrescribir sin preguntar
        '-loglevel', 'error',      # Muestra solo errores
        '-preset', 'fast',         # Usa un preset para optimizar la velocidad
        output_file                 # Archivo de salida
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Archivo MP3 creado en: {output_file}")
        return output_file
    else:
        print(f"Error al procesar el archivo: {result.stderr}")
        raise Exception(f"Error al procesar el archivo: {result.stderr}")