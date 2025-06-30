import requests
from ics import Calendar

# URL do calendário
url = "https://better-f1-calendar.vercel.app/api/calendar.ics"

# Baixa o conteúdo do calendário .ics
response = requests.get(url)
response.raise_for_status()  # Verifica se a solicitação teve sucesso

# Carrega o conteúdo do calendário
calendar = Calendar(response.text)

# Cria um novo calendário para armazenar apenas eventos que têm "Race" no SUMMARY
F1calendar = Calendar()

# Filtra eventos que contêm "Race" no SUMMARY
for event in calendar.events:
    if "Race" in event.name:  # Verifica se "Race" está no nome (summary) do evento
        event.description = None  # Remove a descrição
        event.url = None  # Remove o URL
        F1calendar.events.add(event)

# Serializa o calendário
ics_text = F1calendar.serialize()

# Remove linhas em branco (linhas que só têm espaços ou \n)
lines = [line.strip() for line in ics_text.splitlines() if line.strip() != ""]

# Junta com \r\n (CRLF), conforme exigido pelo padrão .ics
ics_crlf = "\r\n".join(lines) + "\r\n"  # precisa terminar com CRLF também

# Escreve o ficheiro corrigido
with open("F1calendar.ics", "w", encoding="utf-8", newline="") as file:
    file.write(ics_crlf)

print("Ficheiro ICS corrigido criado com sucesso!")
