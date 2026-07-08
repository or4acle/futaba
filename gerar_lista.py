import os
import json

base_dir = "futaba"
lista_final = []

for categoria in os.listdir(base_dir):
    caminho_categoria = os.path.join(base_dir, categoria)
    if os.path.isdir(caminho_categoria):
        for arquivo in os.listdir(caminho_categoria):
            if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.webm', '.webp')):
                lista_final.append({
                    "nome": arquivo,
                    "categoria": categoria,
                    "caminho": f"{categoria}/{arquivo}"
                })

with open('fotos.json', 'w') as f:
    json.dump(lista_final, f)
print(f"Lista {len(lista_final)} gerada! w resenhas bro")

# We got a...
# Victory Royale, yeah, Fortnite we 'bout to get down (Get down!)
# Ten kills on the board right now
# Just wiped out Tomato Town
# My friend just got downed, I revived him now we're heading southbound
# Now we're in the Pleasant Park streets, look at the map, go to the marked sheet
