
import sys, io, traceback
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
mods = ["fastapi","uvicorn","requests","pydantic","moviepy","edge_tts","srt",
        "PIL","imageio_ffmpeg","tenacity","yaml","json_repair","dotenv",
        "arabic_reshaper","bidi","mishkal","multipart","aiofiles","aiohttp"]
bad = []
for m in mods:
    try:
        __import__(m)
    except Exception as e:
        bad.append((m, type(e).__name__+": "+str(e)[:90]))
print("imports OK:", len(mods)-len(bad), "/", len(mods))
for m, e in bad: print("  FALLO", m, "->", e)

# los modulos propios del proyecto
sys.path.insert(0, r"C:\TILINX\agnes")
for m in ["core", "core.api.providers.base", "core.api.key_manager"]:
    try:
        __import__(m); print("proyecto OK:", m)
    except Exception as e:
        print("proyecto FALLO:", m, "->", type(e).__name__+":", str(e)[:120])
