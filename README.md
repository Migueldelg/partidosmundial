# ⚽ Mundial 2026 — Alertas Telegram

Recibe alertas en Telegram de cada partido del Mundial 2026, directamente en tu canal. Sin servidor, sin coste. Funciona con **GitHub Actions**.

- **Partidos de España:** aviso **24 horas antes** + aviso **30 minutos antes**
- **Resto de partidos:** aviso **30 minutos antes**

---

## 🚀 Instalación (5 minutos)

### 1. Fork o crea el repo

Sube estos archivos a un repo en tu GitHub:
```
.github/
  workflows/
    schedule.yml
notify.py
```

### 2. Añade los Secrets

Ve a tu repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Añade estos dos:

| Secret | Valor |
|--------|-------|
| `TELEGRAM_TOKEN` | Token de tu bot (de @BotFather) |
| `TELEGRAM_CHAT_ID` | ID de tu canal (empieza por `-100...`) |

### 3. Activa GitHub Actions

Ve a la pestaña **Actions** de tu repo y confirma que los workflows están activados.

¡Listo! GitHub Actions se encargará del resto.

---

## 📲 Ejemplos de mensajes que recibirás

**Aviso 24h antes (solo partidos de España):**
```
🏆 Mundial 2026
🇪🇸 ¡MAÑANA JUEGA ESPAÑA!

⚽ 🇪🇸 España  vs  🇸🇦 Arabia Saudí

🕐 Mañana a las 18:00h (hora española)
📺 Canal: La 1
📅 21 de junio · Grupo H

¡Prepárate! 🔥
```

**Aviso 30 minutos antes (todos los partidos):**
```
🏆 Mundial 2026
🇪🇸 ¡PARTIDO DE ESPAÑA!

⚽ 🇪🇸 España  vs  🇸🇦 Arabia Saudí

🕐 Hoy a las 18:00h (hora española)
📺 Canal: La 1
📅 21 de junio · Grupo H

¡Empieza en 30 minutos! 🔥
```

---

## ⚙️ Detalles técnicos

- Todos los horarios están en **hora española (CEST, UTC+2)**
- Partidos de España: aviso **24h antes** + aviso **30 minutos antes**
- Resto de partidos: aviso **30 minutos antes**
- Cubre los **104 partidos** de la fase de grupos y eliminatorias
- Los partidos de eliminatorias a partir de dieciseisavos tienen los horarios confirmados pero los equipos aún se desconocen (se actualizará el workflow cuando se conozcan los cruces)

---

## 🔄 Actualizar cruces de eliminatorias

Cuando se conozcan los cruces reales (tras la fase de grupos), edita `schedule.yml` y reemplaza los nombres genéricos como `"Dieciseisavos partido 1"` por los equipos reales.
