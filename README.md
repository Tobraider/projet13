## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Initialiser l'environnement

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- Creer un fichier .env ou initialiser les varaible dans l'environnement directement les variable suivante : 
  - DNS_SENTRY=dnsDuSentry
  - SECRET_KEY=leCleDuProjetDjango

#### Exécuter le site

- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Mise en production

Suivez ces étapes pour déployer l'application `oc_letting_site` en production :

1. **Déploiement avec CircleCI :**
   - À chaque push sur la branche `main` de votre référentiel GitHub, CircleCI est configuré pour déclencher le processus de déploiement automatique.

2. **Serveur de Production :**
   - Assurez-vous que Docker est installé sur votre serveur de production.
   - Créez un réseau Docker pour les conteneurs à l'aide de la commande `docker network create my_network`.

3. **Utilisez Docker Compose pour le Déploiement :**
   - Utilisez le fichier `docker-compose.yml` pour déployer vos services en utilisant `docker-compose up -d`.
   - Les services incluent l'application Django et le serveur Nginx en tant que reverse proxy.

4. **Mises à Jour et Gestion :**
   - Pour mettre à jour l'application, poussez vos modifications sur la branche `main` de votre référentiel GitHub.
   - CircleCI gérera automatiquement le processus de déploiement.

5. **Gestion des Conteneurs :**

   - Utilisez le script `startApp.sh` present sur le serveur en l'appelant comme ceci :

      `source ./startApp.sh`
   
   - Pour charger une ancienne image il suffit d'ajouter le tag de l'image en parametre comme ceci : 

      `source ./startApp.sh tagImage`

   - Pour stopper l'application appelez ce script : 

      `./stopApp.sh`

   Vous n'avez pas besoin de stopper l'appication avant de la demarrer, le script le fait automatiquement

Ces étapes sont une description des étapes pour déployer et gérer l'application `oc_letting_site` en production.
