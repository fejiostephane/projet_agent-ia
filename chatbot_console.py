import subprocess

def run_ollama(prompt):
    """
    Envoie le prompt à Ollama (modèle Mistral)
    et gère les erreurs d'encodage.
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


print("🤖 Chatbot Mistral (Lab 5)")
print("Tape 'quit' pour arrêter.\n")

while True:
    q = input("Vous : ")
    if q.lower() in ["quit", "exit"]:
        print("Agent : À bientôt 👋")
        break

    # Simule la température pour ton analyse (affichage seulement)
    if "créatif" in q.lower() or "poème" in q.lower() or "histoire" in q.lower():
        temp = 0.9
    elif "résume" in q.lower() or "définis" in q.lower() or "explique" in q.lower():
        temp = 0.3
    else:
        temp = 0.7

    print(f"[Température simulée : {temp}]")
    reponse = run_ollama(q)
    print("Agent :", reponse, "\n")
