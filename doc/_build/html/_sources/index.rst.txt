.. oc letting site documentation master file, created by
   sphinx-quickstart on Mon Aug 14 10:57:24 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to oc letting site's documentation!
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Description du Projet
---------------------

Le projet `oc_letting_site` est un site web pour la gestion de locations et de profiles de l'entreprise `Oranges Country Lettings`.

Instructions d'Installation
-----------------------------

1. Assurez-vous d'avoir Python installé sur votre machine.
2. Créez et activez un environnement virtuel :


   Pour Linux :

      | python -m venv venv
      | source venv/bin/activate
      | pip install -r requirements.txt

   Pour Windows : 

      | python -m venv venv
      | .\venv\Scripts\activate
      | pip install -r requirements.txt

3. Configurez les variables d'environnement dans un fichier .env ou via des variables d'environnement pour les valeurs suivantes :

   | DNS_SENTRY
   | SECRET_KEY

Démarrage Rapide
------------------

Pour démarrer l'application :

| Sous Linux :

   | python3 manage.py runserver

| Sous Windows :

   | python manage.py runserver

Technologies et Langages de Programmation
-----------------------------------------

| Django 3.0
| SQLite3 (base de données)
| Langage de Programmation : Python

Structure de la Base de Données et Modèles de Données
------------------------------------------------------

Modèle Profile
^^^^^^^^^^^^^^^

Ce modèle représente les profils d'utilisateurs dans l'application. Il contient des informations sur les utilisateurs et leurs préférences.

+--------------+-----------------------+-----------------------------------+
| Champs       | Type                  | Description                       |
+==============+=======================+===================================+
| user         | ForeignKey (User)     | L'utilisateur associé à ce profil |
| favorite_city| CharField             | Ville préférée de l'utilisateur   |
+--------------+-----------------------+-----------------------------------+

Modèle Address
^^^^^^^^^^^^^^^

Ce modèle représente des adresses, qui peuvent être associées à d'autres modèles tels que Letting.

+------------------+-----------------------+-----------------------------------+
| Champs           | Type                  | Description                       |
+==================+=======================+===================================+
| number           | PositiveIntegerField | Numéro de rue                      |
| street           | CharField             | Nom de la rue                     |
| city             | CharField             | Ville                             |
| state            | CharField             | État (sigle de deux caractères)   |
| zip_code         | PositiveIntegerField | Code postal                        |
| country_iso_code | CharField             | Code ISO du pays (trois lettres)  |
+------------------+-----------------------+-----------------------------------+

Modèle Letting
^^^^^^^^^^^^^^^

Ce modèle représente les éléments de location dans l'application.

+--------------+-----------------------+-----------------------------------+
| Champs       | Type                  | Description                       |
+==============+=======================+===================================+
| title        | CharField             | Titre de la location              |
| address      | ForeignKey (Address)  | Adresse associée à la location    |
+--------------+-----------------------+-----------------------------------+


Interfaces de Programmation
----------------------------

Vues (Views) :
^^^^^^^^^^^^^^^

Les vues de l'application `oc_letting_site` gèrent la logique de traitement des requêtes HTTP et génèrent les réponses appropriées. Voici quelques-unes des vues disponibles :

- `index`: La vue principale qui affiche la page d'accueil du site.
- `profile`: Affiche les détails d'un profil utilisateur.
- `letting`: Affiche les détails d'une location.

Pour utiliser ces vues, référez-vous aux URLs appropriées.

URLs (URL Patterns) :
^^^^^^^^^^^^^^^^^^^^^^^

Les URLs de votre application déterminent la manière dont les vues sont accessibles. Voici quelques exemples d'URLs associées aux vues mentionnées précédemment :

- `/` : Correspond à la vue `index`.
- `/profiles/` : Affiche la liste des `profiles`.
- `/lettings/` : Affiche la liste des `letting`.
- `/profiles/<str:username>/` : Correspond à la vue `profile`.
- `/lettings/<int:letting_id>/` : Correspond à la vue `letting`.

Assurez-vous de consulter les fichiers `urls.py` dans les dossiers des applications pour plus de détails sur les configurations d'URLs.


Guide d'Utilisation
--------------------

Visitez la page d'accueil pour parcourir les profils et les lettings.
Consultez les profils en cliquant sur leur nom d'utilisateur.
Visualisez les informations détaillées d'un letting en cliquant sur son titre.

Procédures de Déploiement et Gestion
-------------------------------------

Pour déployer et gérer l'application `oc_letting_site` en production, vous pouvez suivre les étapes suivantes :

1. **Prérequis :**

   Assurez-vous d'avoir les éléments suivants en place avant de commencer le déploiement :

   - Un environnement avec Docker installé.
   - Un compte Docker Hub avec les informations d'identification nécessaires.

2. **Déploiement avec CircleCI :**

   - Lorsque vous poussez des changements sur la branche `main` de votre référentiel GitHub, CircleCI est configuré pour déclencher automatiquement le processus de déploiement.

   - Dans le fichier `.circleci/config.yml`, sont défini les étapes pour créer une image Docker, la publier sur Docker Hub et ensuite la déployer sur le serveur. Ce processus inclut :

     - Installation des dépendances.
     - Exécution des tests et de la vérification de la couverture.
     - Construction et publication de l'image Docker si les tests réussissent.
     - Mise en place de Nginx comme reverse proxy pour votre application Django.

3. **Serveur de Production :**

   - Sur le serveur de production, assurez-vous d'avoir Docker installé.

   - Créez un réseau Docker pour permettre aux conteneurs de communiquer :
      | docker network create my_network

   - Utilisez Docker Compose pour déployer vos services :
      | docker-compose up -d

4. **Gestion des Mises à Jour :**

   - Pour mettre à jour votre application, suivez ces étapes :

      - Poussez vos modifications sur la branche `main` de votre référentiel GitHub.
      - CircleCI déclenchera le processus de déploiement comme précédemment expliqué.

5. **Gestion des Conteneurs :**

   - Utilisez le script `startApp.sh` present sur le serveur en l'appelant comme ceci :

      | startApp.sh
   
   - Pour charger une ancienne image il suffit d'ajouter le tag de l'image en parametre comme ceci : 

      | startApp.sh tagImage

   - Pour stopper l'application appelez ce script : 

      | stopApp.sh

   Vous n'avez pas besoin de stopper l'appication avant de la demarrer, le script le fait automatiquement

Ces étapes fournissent un aperçu général du processus de déploiement et de gestion de votre application `oc_letting_site` en production.

Références
-----------

Documentation Django : https://docs.djangoproject.com/

Références de Packages
-------------------------

| Django : 3.0
| flake8 : 3.7.0
| pytest-django : 3.9.0
| six : 1.16.0
| pytest-cov : 4.1.0
| sentry-sdk : 1.29.2
| python-dotenv : 1.0.0
| Sphinx : 7.1.2