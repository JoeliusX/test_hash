import hashlib

chemin_fichier = 'hash_joel.pdf'

def hash_fichier(path):
    sha256 = hashlib.sha256()
    try:
        with open(path, 'rb') as f:
            for bloc in iter(lambda: f.read(4096), b''):
                sha256.update(bloc)
        return sha256.hexdigest()
    except FileNotFoundError:
        return "Fichier introuvable."

hash_resultat = hash_fichier(chemin_fichier)
print(f"Hash SHA-256 du fichier : {hash_resultat}")