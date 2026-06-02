import os
import sys
import urllib.request
import urllib.parse
import json

TOKEN   = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
MATCH   = os.environ["MATCH_INFO"]        # passed by the workflow

def send(text: str):
    url  = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id":    CHAT_ID,
        "text":       text,
        "parse_mode": "HTML",
    }).encode()
    req  = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req) as r:
        resp = json.loads(r.read())
    if not resp.get("ok"):
        print("Telegram error:", resp, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    send(MATCH_INFO := MATCH)
    print("Sent:", MATCH_INFO)
