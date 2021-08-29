"""
Program: config.py
Author: HappyPillow918
All the information, not meant to be modified frequently, are stored in this "configuration" file. [Lang: IT]
"""
# ------
# Bot's parameters
# ------

# Bot's token
TOKEN = 'TOKEN'
# Json file path
DATABASE_PATH = 'data/database.json'
BACKUP_PATH = 'data/backups/database-{}.json'
LOGS_PATH = 'data/logs/debug-{}.log'
# Internship group id (only group where /new, /add, /remove commands can be run)
INTERNSHIP_GROUP_ID = 'ID'
# Bot group id (which users are recognized as bot admins)
BOT_GROUP_ID = 'ID'
# Link to the form
FORM_LINK = 'LINK'

# ------
# Bot's text strings
# ------

# Text displayed by running \help in chat
HELP_STRING = """
🧠 *Encefalogramma*
_Help page_

📢 Usa /start per avviare il bot.
"""
# Text displayed by browsing groups menu
MENU_STRINGS = {
    "main": """
🧠 *Encefalogramma*
-- _Menu principale_

In questo bot puoi trovare una lista dei gruppi relativi ai corsi di laurea triennale e magistrale \
di ingegneria biomedica.

_Seleziona il percorso di tuo interesse:_
    """,
    "generic": """
🧠 *Encefalogramma*
-- _Gruppi generici_
    
Esistono tre gruppi generali: uno globale, due per fascia di cognome.
    """,
    "first": """
🧠 *Encefalogramma*
-- _Primo anno_
    
Qui trovi elencati i gruppi dei corsi comuni del primo anno (gestiti dal corso di informatica) \
e il gruppo della materia di indirizzo per il nostro corso.
    """,
    "second": """
🧠 *Encefalogramma*
-- _Secondo anno_
    
Qui trovi elencati i gruppi del secondo anno per il nostro corso.
    """,
    "third": """
🧠 *Encefalogramma*
-- _Terzo anno_
    
Qui trovi elencati i gruppi del terzo anno per il nostro corso. Per i crediti liberi si rimanda a un bot esterno.
    """,
    "about": """
🧠 *Encefalogramma*
-- _Info_

Il bot è rilasciato dietro licenza MIT e il codice può essere consultato su \
[GitHub](https://github.com/HappyPillow918/encefalogramma-bot).

_Se riscontri comportamenti anomali, contatta ----- su Telegram._ 
    """,
    "suggest": """
🧠 *Encefalogramma*
-- _Suggerisci gruppo_

Invia un messaggio qui sotto con il link al gruppo e una breve descrizione dello stesso. Un amministratore \
lo visualizzerà il prima possibile e aggiungerà il gruppo al bot.

⚠ Sono ammessi esclusivamente gruppi *telegram* con cronologia della chat *visibile* ai nuovi membri.
    """,
    "internship": """
🧠 *Encefalogramma*
-- _Tirocinio_
    
Nel gruppo telegram del tirocinio il bot crea autonomamente una lista di coloro che stanno cercando un compagno \
per frequentare il tirocinio ed è possibile utilizzare i seguenti comandi per interagire con essa:
/add |crt+time| - per essere aggiunti alla lista.
/remove - per essere cancellati dalla lista.
/show - per mostrare la lista.
    
_Due esempi di formato atteso dopo il comando /add:_
1. *145F* sta per 145 crediti in Full Time.
2. *132P* sta per 132 crediti in Part Time.
    
Qui sotto trovi il gruppo relativo al tirocinio.
    """,
    "master": """
🧠 *Encefalogramma*
-- _Magistrale_

Qui trovi elencati i gruppi della magistrale di biomedica.
    """
}
# Text asked to confirm suggestions' deletion
ADMIN_CONFIRMATION = "Ho letto i suggerimenti e desidero cancellarli."
# Text displayed by browsing admin menu
ADMIN_STRINGS = {
    "main": """
🧠 *Encefalogramma*
-- _Amministrazione_

Tre funzioni sono disponibili per la gestione del bot.
*[Cancella suggerimenti]* - per cancellare i suggerimenti.
*[Aggiungi]* - per aggiungere gruppi.
*[Rimuovi]* - per rimuovere gruppi.

_I suggerimenti da leggere sono:_
    """,
    "clear": """
🧠 *Encefalogramma*
-- _Cancella suggerimenti_

Scrivi la seguente frase per confermare:
`{text}`
    """,
    "add_group": """
🧠 *Encefalogramma*
-- _Aggiungi un gruppo_

Usa il seguente formato per aggiungere un gruppo:

```
text:
url:
type:
semester:
```
>> _Legenda:_
# *text* - il nome del gruppo.
# *url* - il link al gruppo.
# *type* - il tipo di gruppo. Ammessi: _generic_ (generici), _first_ (primo anno), _second_ (secondo anno), \
_third_ (terzo anno), _internship_ (tirocinio), _master_ (magistrale).
# *semester* - il semestre in cui si colloca. Ammessi: _zero_ (sempre), \
_one_ (primo semestre), _two_ (secondo semestre).
    """,
    "remove_group": """
🧠 *Encefalogramma*
-- _Rimuovi un gruppo_

Scrivi il nome del gruppo che vorresti eliminare:
    """
}
INPUT_STRINGS = {
    "suggest": """
🧠 *Encefalogramma*
-- _Suggerisci gruppo_

✅ Grazie per il tuo contributo! 
Il messaggio è stato registrato correttamente e un amministratore lo controllerà il prima possibile.
    """,
    "clear": """
🧠 *Encefalogramma*
-- _Cancella suggerimenti_

✅ Suggerimenti cancellati! 
    """,
    "add_group": """
🧠 *Encefalogramma*
-- _Aggiungi un gruppo_

✅ Il gruppo è stato aggiunto.
    """,
    "remove_group": """
🧠 *Encefalogramma*
-- _Rimuovi un gruppo_

✅ Il gruppo è stato rimosso.
    """
}
# Suggestions params
SUGGESTIONS_MAXNUM = 3
SUGGESTIONS_MAXCHAR = 1000
# Text displayed by encountering errors.
ERROR_STRINGS = {
    "unknown": """
🧠 *Encefalogramma*
-- _Errore_

⛔ Oh no, questo non sarebbe dovuto accadere. Questa sezione non esiste o non è funzionante.
    """,
    "suggest": """
🧠 *Encefalogramma*
-- _Errore_

⛔ Hai superato il numero massimo di suggerimenti per utente. \
Attendi che un amministratore controlli i suggerimenti inseriti prima di mandarne altri.
    """,
    "add_group": """
🧠 *Encefalogramma*
-- _Errore_

⛔ Il formato non è corretto e il gruppo non è stato inserito. Riprovare.
    """,
    "remove_group": """
🧠 *Encefalogramma*
-- _Errore_

⛔ Il nome del gruppo inserito non è stato trovato. Riprovare.
    """,
    "clear": """
🧠 *Encefalogramma*
-- _Errore_

⛔ Il messaggio di conferma non corrisponde a quello atteso. Riprovare.
    """
}
# Text displayed in logs
LOGS_STRINGS = {
    "suggest": """
🧠 *Encefalogramma*
-- _Papyrus_

🆕 {name} ha aggiunto questo suggerimento:
{text}
    """,
    "clear": """
🧠 *Encefalogramma*
-- _Papyrus_

🔠 {name} ha cancellato tutti i suggerimenti!{text}
    """,
    "add_group": """
🧠 *Encefalogramma*
-- _Papyrus_

🔠 {name} ha aggiunto il gruppo {text}!
    """,
    "remove_group": """
🧠 *Encefalogramma*
-- _Papyrus_

🔠 {name} ha rimosso il gruppo {text}!
    """,
}
# Text displayed by running internship commands
INTERNSHIP_STRINGS = {
    "list": """
👩‍🚀 *Coppie Tirocinio*

/add |crt+time| - per essere aggiunti alla lista.
/remove - per essere cancellati dalla lista.
/show - per mostrare la lista.

_In cerca di compagno:_
    """,
    "new": """
👩‍🚀 *Coppie Tirocinio*

_Una nuova lista è stata creata per il tirocinio {period}._
    """,
    "add": """
👩‍🚀 *Coppie Tirocinio*

_{name} sta cercando un compagno ed è stato aggiunto alla lista!_
    """,
    "remove": """
👩‍🚀 *Coppie Tirocinio*

_{name} ha trovato un compagno ed è stato rimosso dalla lista!_
    """,
    "error": """
👩‍🚀 *Coppie Tirocinio*

_Hai immesso un formato invalido. Ecco due esempi di formato atteso dopo il comando /add:_
1. *145F* sta per 145 crediti in Full Time
2. *132P* sta per 132 crediti in Part Time
    """
}
