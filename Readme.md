# Chat Neov

Chat Neov est une application interactive développée avec Streamlit, permettant aux utilisateurs de télécharger des fichiers PDF ou TXT et d'interagir avec leur contenu via un chatbot intuitif.

## Table des Matières

- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Architecture du Projet](#architecture-du-projet)
- 

## Fonctionnalités

- **Téléchargement de Fichiers** : Chargez vos documents PDF ou TXT directement depuis l'interface utilisateur.
- **Chatbot Intégré** : Posez des questions et obtenez des réponses basées sur le contenu de vos documents.
- **Traitement en Temps Réel** : Analyse instantanée des documents pour des interactions fluides et efficaces.


## Installation

Suivez les étapes ci-dessous pour installer et configurer l'application :

1. **Cloner le Dépôt** :

   ```bash
   git clone https://github.com/hachim001/LLM-neov.git
   cd LLM-neov
   ```

2. **Créer un Environnement Virtuel** (recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez venv\Scripts\activate
   ```

3. **Installer les Dépendances** :

   ```bash
   pip install -r requirements.txt
   ```



4. **Lancer l'Application** :

   ```bash
   streamlit run neovLLM.py
   ```

   Accédez ensuite à l'application via votre navigateur à l'adresse indiquée dans le terminal.

## Utilisation

1. **Téléchargement de Fichiers** :

   Dans la colonne de gauche de l'application, cliquez sur "Choisissez des fichiers" pour importer vos documents PDF ou TXT.

2. **Interaction avec le Chatbot** :

   Dans la colonne de droite, posez vos questions en utilisant le champ de saisie en bas de la page. Le chatbot analysera le contenu des documents téléchargés pour fournir des réponses pertinentes.

## Architecture du Projet

Le projet est structuré de la manière suivante :

```
LLM NEOV/
├── neovLLM.py
├── requirements.txt
├── .env
├── chroma_db/
└── README.md
```

- **neovLLM.py** : Script principal de l'application, gérant l'interface utilisateur, le téléchargement des fichiers et l'interaction avec le chatbot.
- **requirements.txt** : Liste des dépendances Python nécessaires à l'exécution de l'application.
- **.env** : Fichier contenant les variables d'environnement, telles que les clés API pour HuggingFace et Groq.
- **chroma_db/** : Répertoire où sont stockées les bases de données vectorielles créées lors de l'exécution.
- **README.md** : Ce fichier, fournissant une vue d'ensemble du projet.





