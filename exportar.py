import os

# Carpetas y archivos a ignorar
IGNORAR_CARPETAS = {'.git', '__pycache__', '.venv', 'venv', '.pytest_cache', '.idea', '.vscode'}
EXTENSIONES_PERMITIDAS = {'.py', '.ini', '.txt', '.md', '.json', '.yaml', '.yml','csv','png','html'}

with open('codigo_completo_pom.txt', 'w', encoding='utf-8') as salida:
    for raiz, carpetas, archivos in os.walk('.'):
        # Filtrar carpetas ignoradas
        carpetas[:] = [c for c in carpetas if c not in IGNORAR_CARPETAS]
        
        for archivo in archivos:
            if archivo == 'exportar.py' or archivo == 'codigo_completo_pom.txt':
                continue
            
            _, ext = os.path.splitext(archivo)
            if ext in EXTENSIONES_PERMITIDAS:
                ruta_completa = os.path.join(raiz, archivo)
                salida.write(f"{'='*60}\n")
                salida.write(f"ARCHIVO: {ruta_completa}\n")
                salida.write(f"{'='*60}\n\n")
                
                with open(ruta_completa, 'r', encoding='utf-8', errors='ignore') as f:
                    salida.write(f.read() + "\n\n")

print("¡Listo! Todo el código se exportó a 'codigo_completo_pom.txt'")