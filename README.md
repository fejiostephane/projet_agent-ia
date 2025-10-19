# 🤖 Reactive AI Agent — Ydays M1 IA 2025

## 🧠 Description
Ce projet implémente un **agent réactif d’intelligence artificielle** utilisant **Ollama (modèle Mistral)** en local.  
L’agent reçoit un texte en entrée, le transmet à un modèle de langage local, et affiche la réponse instantanément.  
Deux versions sont disponibles :
- **Chatbot Console** (interaction texte dans le terminal)
- **Chatbot Streamlit** (interface web graphique locale)

Ce travail s’inscrit dans le cadre du module *“Agents d’IA — Ydays 2025”*.

---

## ⚙️ Installation

### 🧩 Prérequis
- **Python ≥ 3.11**
- **Ollama installé localement** :  
  👉 [https://ollama.com/download](https://ollama.com/download)
- (Optionnel) **Docker** si tu veux exécuter le projet dans un conteneur.

---

### 💻 Exécution locale (console)
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/<ton-utilisateur>/ai-agent-lab.git
   cd ai-agent-lab
Installer les dépendances :

pip install -r requirements.txt


Vérifier qu’Ollama et Mistral fonctionnent :

ollama run mistral "Bonjour !"


Lancer l’agent console :

python chatbot_console.py

🖥️ Exécution avec interface Streamlit

Lancer l’application :

streamlit run chatbot_ui.py


Ouvrir le navigateur :
👉 http://localhost:8501

🐳 Exécution avec Docker
🧱 Construction de l’image
docker build -t ai-agent-lab .

🚀 Lancement du conteneur
docker run --rm -it -v ~/.ollama:/root/.ollama ai-agent-lab


💡 Le volume ~/.ollama:/root/.ollama permet de partager tes modèles Ollama locaux avec le conteneur (sans retéléchargement de Mistral).

🌐 (Option : interface Streamlit dans Docker)

Modifie la dernière ligne de ton Dockerfile :

CMD ["streamlit", "run", "chatbot_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]


Lance :

docker run -p 8501:8501 -v ~/.ollama:/root/.ollama ai-agent-lab


Ouvre ton navigateur sur :
👉 http://localhost:8501

🧩 Fonctionnement

Pipeline :

Entrée utilisateur → Modèle Mistral (via Ollama) → Réponse générée → Affichage console / web


L’agent fonctionne en mode réactif :
il perçoit la question, l’envoie au modèle, et affiche la réponse immédiatement, sans mémoire persistante.

📁 Structure du projet
ai-agent-lab/
├── src/
│   └── main.py               # Agent réactif principal (Lab 4)
├── chatbot_console.py         # Version console (Lab 5)
├── chatbot_ui.py              # Interface Streamlit (Lab 5 option)
├── requirements.txt           # Dépendances Python
├── Dockerfile                 # Configuration Docker (Lab 8)
├── .env.example               # Variables d’environnement (exemple)
└── README.md                  # Documentation (Lab 9)

🧪 Exemples d’utilisation

Mode console :

🤖 Chatbot Mistral (Lab 5)
Tape 'quit' pour arrêter.

Vous : Explique-moi ce qu’est un agent d’IA.
[Température simulée : 0.3]
Agent : Un agent d’intelligence artificielle est un système capable de percevoir, raisonner et agir pour atteindre un objectif.


Mode Streamlit :

Interface web avec champ de texte, curseur de température et bouton “Envoyer”.
La réponse du modèle s’affiche proprement sous le champ.

📦 Fichiers importants
Fichier	Rôle
chatbot_console.py	Chatbot texte dans le terminal
chatbot_ui.py	Interface web avec Streamlit
requirements.txt	Liste des dépendances Python
Dockerfile	Conteneurisation du projet
.env.example	Exemple de configuration d’API
README.md	Documentation du projet
📘 Évaluation (résumé des Labs)
Lab	Sujet	Livrable
Lab 1	Installation Ollama	Capture d’écran du test réussi
Lab 2	Comparaison Local vs API	Tableau + commentaire
Lab 3	Prompt Engineering	Tableau + observation
Lab 4	Agent Réflexe	Code + capture
Lab 5	Mini Chatbot complet	Code + capture / vidéo
Lab 6	Évaluation des réponses	Tableau + analyse
Lab 7	Structuration Git	Lien GitHub fonctionnel
Lab 8	Dockerisation	Capture du build et run
Lab 9	README Professionnel	Ce fichier
👨‍💻 Auteur

Nom Prénom — Ydays M1 IA 2025
📧 ton.email@exemple.com

📍 Campus Ynov — Master 1 Intelligence Artificielle