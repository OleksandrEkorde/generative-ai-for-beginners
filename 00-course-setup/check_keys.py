"""Перевірка API-ключів із файлу .env (практична робота 1, пункт 5.2).

Запуск з кореня репозиторію:  python 00-course-setup/check_keys.py
Використовує лише стандартну бібліотеку Python. Значення ключів не виводяться.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent / ".env"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/"


def load_env():
    """Значення з .env, доповнені змінними середовища (секрети Codespaces)."""
    values = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8-sig").splitlines():
            match = re.match(r"\s*([A-Z_]+)\s*=\s*(?:'([^']*)'|\"([^\"]*)\"|([^#]*))", line)
            if match:
                value = next(g for g in match.groups()[1:] if g is not None)
                values[match.group(1)] = value.strip()
    values.update({k: v for k, v in os.environ.items() if k.startswith(("GEMINI_", "HUGGING_FACE_"))})
    return values


def is_set(value):
    return bool(value) and not value.startswith("<")


def request(url, headers, body=None):
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json", **headers})
    with urllib.request.urlopen(req, timeout=180) as response:
        return json.load(response)


def check(name, action):
    try:
        print(f"[OK]    {name}: {action()}")
        return True
    except urllib.error.HTTPError as error:
        try:
            details = json.load(error)["error"]
            message = details["message"] if isinstance(details, dict) else details
        except (ValueError, KeyError):
            message = error.reason
        print(f"[ПОМИЛКА] {name}: HTTP {error.code} - {message}")
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"[ПОМИЛКА] {name}: немає з'єднання - {error}")
    return False


def main():
    env = load_env()
    ok = True

    key = env.get("GEMINI_API_KEY")
    if not is_set(key):
        print("[ПОМИЛКА] Gemini: GEMINI_API_KEY не заповнений у файлі .env")
        ok = False
    else:
        headers = {"x-goog-api-key": key}
        model = env.get("GEMINI_MODEL") or "gemini-3.8-flash"
        embedding = env.get("GEMINI_EMBEDDING_MODEL") or "gemini-embedding-001"

        def generate():
            request(f"{GEMINI_URL}{model}:generateContent", headers,
                    {"contents": [{"parts": [{"text": "Reply with the word OK"}]}]})
            return f"модель {model} відповідає"

        def embed():
            result = request(f"{GEMINI_URL}{embedding}:embedContent", headers,
                             {"content": {"parts": [{"text": "test"}]}})
            return f"модель {embedding}, вектор із {len(result['embedding']['values'])} чисел"

        ok &= check("Gemini (текст)", generate)
        ok &= check("Gemini (вбудовування)", embed)

    token = env.get("HUGGING_FACE_API_KEY")
    if not is_set(token):
        print("[ПРОПУЩЕНО] Hugging Face: HUGGING_FACE_API_KEY не заповнений")
    else:
        def whoami():
            request("https://huggingface.co/api/whoami-v2", {"Authorization": f"Bearer {token}"})
            return "токен дійсний"

        ok &= check("Hugging Face", whoami)

    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
