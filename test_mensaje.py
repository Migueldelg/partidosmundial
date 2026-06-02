import urllib.request, urllib.parse, json, os

# Carga el .env manualmente (sin dependencias externas)
with open(".env") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())

TOKEN   = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send(text):
    url  = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}).encode()
    req  = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req) as r:
        resp = json.loads(r.read())
    return resp.get("ok")

mensajes = [
    # 1. Aviso 24h antes — España
    ("""🏆 <b>Mundial 2026</b>
🇪🇸 <b>¡MAÑANA JUEGA ESPAÑA!</b>

⚽ 🇪🇸 España  vs  🇸🇦 Arabia Saudí

🕐 Mañana a las <b>18:00h</b> (hora española)
📺 Canal: <b>La 1</b>
📅 21 de junio · Grupo H

<b>¡Prepárate! 🔥</b>""", "Aviso 24h — España"),

    # 2. Aviso 30min antes — España
    ("""🏆 <b>Mundial 2026</b>
🇪🇸 <b>¡PARTIDO DE ESPAÑA!</b>

⚽ 🇪🇸 España  vs  🇸🇦 Arabia Saudí

🕐 Hoy a las <b>18:00h</b> (hora española)
📺 Canal: <b>La 1</b>
📅 21 de junio · Grupo H

<b>¡Empieza en 30 minutos! 🔥</b>""", "Aviso 30min — España"),

    # 3. Aviso 30min antes — otro partido
    ("""🏆 <b>Mundial 2026</b>

⚽ 🇧🇷 Brasil  vs  🇲🇦 Marruecos

🕐 Hoy a las <b>00:00h</b> (hora española)
📺 Canal: <b>La 1</b>
📅 14 de junio · Grupo C

<b>¡Empieza en 30 minutos! 🔥</b>""", "Aviso 30min — Brasil vs Marruecos"),
]

for msg, nombre in mensajes:
    ok = send(msg)
    print(f"{'✅' if ok else '❌'} {nombre}")
