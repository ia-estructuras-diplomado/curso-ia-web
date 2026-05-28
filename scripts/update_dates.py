import os
import re

# Mapping of replacements for dates and texts
replacements = {
    # Full Spanish dates
    "Martes, 5 de Agosto de 2026": "Jueves, 28 de Mayo de 2026",
    "Jueves, 7 de Agosto de 2026": "Martes, 2 de Junio de 2026",
    "Martes, 12 de Agosto de 2026": "Jueves, 4 de Junio de 2026",
    "Jueves, 14 de Agosto de 2026": "Martes, 9 de Junio de 2026",
    "Martes, 19 de Agosto de 2026": "Jueves, 11 de Junio de 2026",
    "Jueves, 21 de Agosto de 2026": "Martes, 16 de Junio de 2026",
    "Martes, 26 de Agosto de 2026": "Jueves, 18 de Junio de 2026",
    "Jueves, 28 de Agosto de 2026": "Martes, 23 de Junio de 2026",

    "Martes, 5 de Agosto": "Jueves, 28 de Mayo",
    "Jueves, 7 de Agosto": "Martes, 2 de Junio",
    "Martes, 12 de Agosto": "Jueves, 4 de Junio",
    "Jueves, 14 de Agosto": "Martes, 9 de Junio",
    "Martes, 19 de Agosto": "Jueves, 11 de Junio",
    "Jueves, 21 de Agosto": "Martes, 16 de Junio",
    "Martes, 26 de Agosto": "Jueves, 18 de Junio",
    "Jueves, 28 de Agosto": "Martes, 23 de Junio",

    # Simple dates
    "5 de Agosto de 2026": "28 de Mayo de 2026",
    "7 de Agosto de 2026": "2 de Junio de 2026",
    "12 de Agosto de 2026": "4 de Junio de 2026",
    "14 de Agosto de 2026": "9 de Junio de 2026",
    "19 de Agosto de 2026": "11 de Junio de 2026",
    "21 de Agosto de 2026": "16 de Junio de 2026",
    "26 de Agosto de 2026": "18 de Junio de 2026",
    "28 de Agosto de 2026": "23 de Junio de 2026",

    "5 de Agosto": "28 de Mayo",
    "7 de Agosto": "2 de Junio",
    "12 de Agosto": "4 de Junio",
    "14 de Agosto": "9 de Junio",
    "19 de Agosto": "11 de Junio",
    "21 de Agosto": "16 de Junio",
    "26 de Agosto": "18 de Junio",
    "28 de Agosto": "23 de Junio",
    "26-28 de Agosto": "18-23 de Junio",

    # Short dates
    "5 Ago": "28 May",
    "12 Ago": "4 Jun",
    "14 Ago": "9 Jun",
    "21 Ago": "16 Jun",
    "26 Ago": "18 Jun",
    "28 Ago": "23 Jun",

    # General references
    "Agosto 2026": "Mayo - Junio 2026",
    "Agosto de 2026": "Mayo - Junio de 2026",
    "28 de agosto": "23 de junio",
    "Antes del 5 de Agosto": "Antes del 28 de Mayo",
    
    # Calendar visualization in cronograma.md
    """Agosto 2026
SEMANA 1:  Lunes 4  |  Martes 5 *(SES 1)  |  Miércoles 6  |  Jueves 7 *(SES 2)  |  Viernes 8
SEMANA 2:  Lunes 11 |  Martes 12 *(SES 3) |  Miércoles 13 |  Jueves 14 *(SES 4) |  Viernes 15
SEMANA 3:  Lunes 18 |  Martes 19 *(SES 5) |  Miércoles 20 |  Jueves 21 *(SES 6) |  Viernes 22
SEMANA 4:  Lunes 25 |  Martes 26 *(SES 7) |  Miércoles 27 |  Jueves 28 *(SES 8) |  Viernes 29""":
    """Mayo - Junio 2026
SEMANA 1 (May 25):  Lunes 25 | Martes 26 | Miércoles 27 | Jueves 28 *(SES 1) | Viernes 29
SEMANA 2 (Jun 01):  Lunes 1  | Martes 2 *(SES 2)  | Miércoles 3  | Jueves 4 *(SES 3)  | Viernes 5
SEMANA 3 (Jun 08):  Lunes 8  | Martes 9 *(SES 4)  | Miércoles 10 | Jueves 11 *(SES 5) | Viernes 12
SEMANA 4 (Jun 15):  Lunes 15 | Martes 16 *(SES 6) | Miércoles 17 | Jueves 18 *(SES 7) | Viernes 19
SEMANA 5 (Jun 22):  Lunes 22 | Martes 23 *(SES 8) | Miércoles 24 | Jueves 25 | Viernes 26"""
}

docs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))

def process_file(file_path):
    print(f"Processing: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            modified = True
            
    # Also handle some regexes if needed
    # (e.g. any leftover 'de Agosto' cases)
    
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Updated!")

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            process_file(os.path.join(root, file))

print("Date replacement finished!")
