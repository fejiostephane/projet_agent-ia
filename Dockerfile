# ================================
# 🐳 Dockerfile — Lab 8 (Ydays)
# ================================

# Étape 1 — Image de base
FROM python:3.11-slim

# Étape 2 — Dossier de travail dans le conteneur
WORKDIR /app

# Étape 3 — Copier le fichier de dépendances
COPY requirements.txt .

# Étape 4 — Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 — Copier tout le projet dans le conteneur
COPY . .

# Étape 6 — Commande de démarrage par défaut
# Ici, on lance ton agent console (tu peux changer pour chatbot_ui.py si tu veux l’interface Streamlit)
CMD ["python", "chatbot_console.py"]
