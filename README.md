# OptimaDeck

OptimaDeck est une application de gestion de tâches conçue pour optimiser la collaboration et la productivité des équipes. 

## Structure des fichiers

### 1. `app.py`
Un serveur Flask:
- **Lecture de variables d'environnement** : Exposition de clés via `/config`.
- **Exécution de commandes** : Endpoint `/run` permettant l'exécution de commandes.

### 2. `requirements.txt`
Liste des dépendances de l'application.

### 3. `Dockerfile`
Un fichier de configuration Docker.

### 4. `ci-cd-pipeline.yml`
Un pipeline CI/CD.

## Prérequis
- **Python 3.9** ou une version ultérieure
- **Docker** pour exécuter et construire l'application
- **Un environnement isolé** (ex. : VM ou conteneur)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <url_du_dépôt>
   cd OptimaDeck
   ```

2. Installez les dépendances dans un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Lancez le serveur Flask :
   ```bash
   python app.py
   ```

## Utilisation

- **Endpoint `/config`** : Affiche la clé.
- **Endpoint `/run`** : Permet d'exécuter des commandes système passées en paramètre via `?cmd=`.

Exemple :
```bash
curl http://localhost:5000/run?cmd=ls
```

## Pipeline CI/CD

Le fichier `ci-cd-pipeline.yml` inclut des étapes pour :
1. Installer les dépendances.
2. Construire une image Docker.
3. Déployer l'application avec des permissions.

## Licence
Ce projet est fourni sous licence [MIT](LICENSE), utilisable à des fins éducatives.


