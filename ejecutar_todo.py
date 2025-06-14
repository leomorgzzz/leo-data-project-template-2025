import subprocess

scripts = [
    
]

for script in scripts:
    print(f"\nEjecutando {script}...")
    resultado = subprocess.run(["python", script])
    if resultado.returncode != 0:
        print(f"Error al ejecutar {script}. Deteniendo ejecución.")
        break

print("\nProceso completo.")
