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

msg = """🏆 <b>Mundial 2026</b>
🇪🇸 <b>¡PARTIDO DE ESPAÑA!</b>

⚽ 🇪🇸 España  vs  🇸🇦 Arabia Saudí

🕐 Hoy a las <b>18:00h</b> (hora española)
📺 Canal: <b>La 1</b>
📅 21 de junio · Grupo H

¡Empieza en 30 minutos! 🔥"""

url  = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}).encode()
req  = urllib.request.Request(url, data=data, method="POST")
with urllib.request.urlopen(req) as r:
    resp = json.loads(r.read())
print("✅ Enviado!" if resp.get("ok") else resp)
