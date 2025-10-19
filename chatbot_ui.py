import streamlit as st
import subprocess

# -----------------------------
# Configuration de la page
# -----------------------------
st.set_page_config(page_title="Mini Chatbot Mistral", page_icon="🤖")
st.title("💬 Mini Chatbot — Lab 5 (Ollama + Streamlit)")
st.write("Pose une question à ton agent Mistral local ! Tape une phrase, choisis la température, et clique sur *Envoyer*.")

# -----------------------------
# Fonction pour appeler Ollama
# -----------------------------
def run_ollama(prompt):
    """
    Exécute Ollama (modèle Mistral) depuis Python et renvoie la réponse.
    Gère l'encodage et les erreurs pour Windows.
    """
    try:
        r = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        if r.returncode != 0:
            return f"❌ Erreur Ollama : {r.stderr.strip()}"
        return r.stdout.strip() if r.stdout else "⚠️ Pas de réponse du modèle."

    except Exception as e:
        return f"❌ Erreur Python : {e}"

# -----------------------------
# Interface utilisateur Streamlit
# -----------------------------
st.divider()
prompt = st.text_area("💭 Entrez votre question :", placeholder="Ex: Explique-moi ce qu’est un agent d’IA.")
temperature = st.slider("🔥 Température (créativité simulée)", 0.1, 1.0, 0.7, 0.1)

if st.button("🚀 Envoyer la requête"):
    if prompt.strip() == "":
        st.warning("⚠️ Merci d’écrire une question avant d’envoyer.")
    else:
        st.info(f"Température simulée : **{temperature}**")
        with st.spinner("🧠 Réflexion en cours..."):
            response = run_ollama(prompt)
        st.success("✅ Réponse reçue :")
        st.write(response)

st.divider()
st.caption("💡 Propulsé par Ollama + Mistral | Module 1 — Ydays M1 IA")
