# 🛡️ SSH Monitor Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Un tableau de bord interactif pour visualiser et analyser les tentatives d'intrusion SSH. Ce projet transforme des logs bruts en graphiques exploitables pour les équipes de sécurité.

🔗 **Démo Live :** [Accéder à l'application](https://sshmonitor-pngrw8qvgrkhbucu2537kh.streamlit.app)

## 📋 Fonctionnalités

*   **KPIs en temps réel** : Total des attaques, adresses IP uniques, attaquant principal.
*   **Filtrage Dynamique** :
    *   Par type d'événement (Échec de mot de passe, Connexion fermée, etc.).
    *   Par adresse IP source (Multi-sélection).
*   **Visualisations** :
    *   📊 Top 5 des adresses IP les plus agressives.
    *   📈 Chronologie des attaques (Time Series).
*   **Exploration** : Accès aux logs bruts détaillés via un tableau interactif.

## 🛠️ Installation et Lancement local

Si vous souhaitez faire tourner l'application sur votre propre machine :

1.  **Cloner le dépôt**
    ```
    git clone https://github.com/DHAIMINI-HAMID/ssh_monitor.git
    cd ssh_monitor
    ```

2.  **Installer les dépendances**
    ```
    pip install -r requirements.txt
    ```

3.  **Lancer l'application**
    ```
    streamlit run app.py
    ```

## 📂 Structure du projet

*   `app.py` : Le code source principal de l'application Streamlit.
*   `dataset_ssh.csv` : Jeu de données contenant les logs nettoyés.
*   `requirements.txt` : Liste des librairies Python nécessaires.

## 👤 Auteur

**DHAIMINI-HAMID**
*   IT Infrastructure & Cybersecurity Enthusiast
