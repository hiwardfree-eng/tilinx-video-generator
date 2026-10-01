# 🎬 TilinX Video Generator

Generador **autónomo de videos cortos con IA** — escribe un artículo o guion y obtén un video vertical 9:16 completo: escenas, voz TTS, subtítulos y música. Incluye puente para **publicar directo en TikTok**.

> Rebrand total de un proyecto open-source de video IA. Instalación limpia, marca TilinX.

---

## ✨ Qué hace

| Entrada | Salida |
|---|---|
| Artículo / guion / poema (texto) | Video **9:16 vertical**, auto-dividido en escenas |
| — | Voz TTS (`es-ES` por defecto, 200+ voces/22 idiomas) |
| — | Subtítulos quemados, estilos ajustables |
| — | Referencia de imagen opcional por escena |
| — | **Puente TikTok**: el video se sube solo al perfil |

## 🚀 Instalación (Windows)

```bash
# 1. clonar
git clone https://github.com/hiwardfree-eng/tilinx-video-generator.git
cd tilinx-video-generator

# 2. python 3.10+
python -m venv .venv
.venv\Scripts\pip install -r requirements_clean.txt

# 3. tu API key (gratis en platform.agnes-ai.com)
copy .env.example .env
# editar .env → pon tu key en TILINX_API_KEY

# 4. arrancar
python server.py
# → abrir http://localhost:8765
```

> ⚠️ El `.env` **no se sube** al repo. `requirements.txt` original puede traer comentarios con bytes no-utf8; usar `requirements_clean.txt`.

### Frontend (desde fuente)
```bash
cd frontend
npm install
npm run build   # regenera static/assets
```

## 🎬 Flujo autónomo (TilinX → TikTok)

```bash
node tiktok-pipeline/tilinx-autonomo.js "tu artículo aquí" "caption del video"
```
1. Crea tarea en el generador local (`:8765`)
2. Espera el render 9:16
3. Publica en TikTok con la sesión guardada (`~/.playwright-tiktok`)

## 🔑 Configuración (.env)

```env
TILINX_API_KEY=your-key
HOST=0.0.0.0
PORT=8765
TILINX_RATE_LIMIT=160
TILINX_RATE_BURST=32
```

> Compatibilidad: también se lee `AGNES_API_KEY` como fallback (proyectos que migran).

## 📦 API principal

- `POST /api/tasks/manuscript` — artículo → video (variantes: simple, creative, poetry, anchor)
- `GET /api/tasks/{id}` — estado de la tarea
- `GET /api/gallery` — videos generados
- `POST /api/image/generate` — generación de imágenes

## 🧩 Estructura

```
core/            # api (chat, image, video), config, audio, compositor
web/             # FastAPI routes (tasks, gallery, config, health)
frontend/        # UI Vue 3 + Vite (compilada a static/)
static/          # assets servidos (index + bundles)
resource/        # fuentes y recursos
pipeline/        # (tiktok) publish.py — subida autónoma
tilinx-autonomo.js  # puente video → TikTok
```

## ⚖️ Licencia

MIT — original agradece upstream; este proyecto es el rebrand TilinX.

---

Hecho con ❤️ por **TilinX (H Bencosme)** — creador de tilinXcode.

---

## 🙏 Créditos

APIs, backend, tareas e interfaz original: **Agnes Video Generator** (https://platform.agnes-ai.com). Este repo es un rebrand TilinX sobre su código abierto. Ver ATTRIBUTION.md.
