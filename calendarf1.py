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

# Salva o novo calendário em um arquivo .ics
# Salva o novo calendário em um arquivo .ics com codificação UTF-8
with open("F1calendar.ics", "w", encoding="utf-8") as file:
    file.writelines(F1calendar.serialize())


print("Novo arquivo 'F1calendar.ics' criado com sucesso!")
