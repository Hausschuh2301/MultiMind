# 🧠 MULTIMIND – KI-Aggregator (lokal + API)

MULTIMIND kombiniert mehrere KI-Modelle (lokal und per API), um die besten Antworten zu generieren und diese zusammenzufassen.

---

## Features

- Unterstützung lokaler KI-Modelle (z.B. via Ollama)  
- API-Integration (OpenAI, Claude, u.a.)  
- Automatische Antwort-Kombination und Zusammenfassung  
- Konfigurierbar über YAML-Dateien  
- Benutzeroberfläche mit Streamlit  

---

## Projektstruktur

```
MULTIMIND/
├── configs/             # Konfigurationsdateien (models.yaml)
├── core/                # Kernlogik, Modell-Wrapper, Prompt-Router
├── ui/                  # Streamlit-Oberfläche
├── .env.example         # Beispiel-Umgebungsvariablen
├── requirements.txt     # Python-Abhängigkeiten
└── README.md            # Dieses Dokument
```

---

## Installation

1. Repository klonen:

```bash
git clone https://github.com/Hausschuh2301/MultiMind.git
cd MultiMind
```

2. Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

3. (Optional) Lokale KI-Modelle einrichten (z.B. Ollama):

```bash
bash scripts/setup_ollama.sh
```

---

## Nutzung

### Streamlit starten:

```bash
streamlit run ui/streamlit_app.py
```

### Modelle konfigurieren

Passe `configs/models.yaml` an, um API-Keys, Modellnamen und Aktivierung zu steuern.

---

## Lizenz

MIT Lizenz

---

## Autor

<<<<<<< HEAD
TimHa – 2025  
=======
<<<<<<< HEAD
<<<<<<< HEAD
Hausschuh2301 – 2025  
=======
TimHa – 2025  
>>>>>>> 131c861 (Buffixes // Fix OpenAI wrapper for openai v0.28.0 compatibility)
=======
Hausschuh2301 – 2025  
>>>>>>> b7ca9b71f202500506c81444444be644caa716be
>>>>>>> 48f90b8 (Buffixes // Fix OpenAI wrapper for openai v0.28.0 compatibility)
GitHub: [Hausschuh2301](https://github.com/Hausschuh2301)

---

## Support

Fragen oder Probleme? Issues öffnen unter:  
https://github.com/Hausschuh2301/MultiMind/issues