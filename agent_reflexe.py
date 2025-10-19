import subprocess

def reactive_agent(prompt):
    """
    Envoie le prompt à Ollama (modèle Mistral) et récupère la réponse en UTF-8.
    """
    r = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",      # ✅ Correction importante
        errors="ignore"        # évite le crash si un caractère est inconnu
    )
    return r.stdout.strip()

print("🤖 Agent réflexe Mistral (tape 'quit' pour arrêter)\n")

while True:
    q = input("Vous : ")
    if q.lower() in ["quit", "exit"]:
        print("Agent : À bientôt 👋")
        break
    reponse = reactive_agent(q)
    print("Agent :", reponse)
