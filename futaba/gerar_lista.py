import os
import json

caminho = "futaba/futaba"
arquivos = [f for f in os.listdir(caminho) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webm'))]

with open('fotos.json', 'w') as f:
    json.dump(arquivos, f)

print(f"eba {len(arquivos)} arquivos adicionados no fotos.json")