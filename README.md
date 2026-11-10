# Nasus Nasus – Regelbuch

Lesbare Fassung des Regelwerks **Nasus Nasus**, veröffentlicht als Website:
<https://njebich.github.io/nasus-nasus-regelbuch/>

## Rechte

© njebich. Alle Rechte vorbehalten. Lesen und Nutzung als Spielregelwerk für private Spielrunden sind gestattet, alles darüber hinaus nur mit vorheriger Zustimmung. Der vollständige Vorbehalt steht in [RIGHTS.md](RIGHTS.md).

Es gilt keine Open-Source- oder Creative-Commons-Lizenz für die Regelbuchinhalte.

## Aufbau dieses Repositorys

- `regelbuch/` – die Kapitel als Markdown (Obsidian-Syntax). **Wird automatisch aus dem privaten Projekt befüllt. Änderungen hier werden beim nächsten Export überschrieben.**
- `build.py`, `site/`, `requirements.txt` – kleiner Website-Build (Wiki-Links werden beim Build in normale Links umgewandelt).
- `.github/workflows/pages.yml` – baut und veröffentlicht die Website bei jedem Push.
- `RIGHTS.md` – Rechtevorbehalt.

## Technik

Der Build verwendet [Python-Markdown](https://python-markdown.github.io/) (BSD-3-Clause-Lizenz). Die Bibliothek wird beim Build installiert und ist nicht Teil dieses Repositorys. Diese Lizenz betrifft nur die Technik, nicht die Regelbuchinhalte.
