# Налаштування середовища розробки

Ми налаштували цей репозиторій та курс з [контейнером розробки](https://containers.dev), який має універсальне середовище виконання, що підтримує розробку на Python3, .NET, Node.js та Java. Відповідна конфігурація визначена у файлі `devcontainer.json`, розташованому в папці `.devcontainer/` в корені цього репозиторію.

Щоб активувати контейнер розробки, запустіть його в [GitHub Codespaces](https://docs.github.com/en/codespaces/overview) (для хмарного середовища виконання) або в [Docker Desktop](https://docs.docker.com/desktop/) (для локального середовища виконання). Прочитайте [цю документацію](https://code.visualstudio.com/docs/devcontainers/containers) для отримання додаткової інформації про те, як працюють контейнери розробки в VS Code.

> [!ПОРАДА]
> Ми рекомендуємо використовувати GitHub Codespaces для швидкого старту з мінімальними зусиллями. Він надає щедру [безкоштовну квоту](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts) для персональних облікових записів. Налаштуйте [таймаути](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces) для зупинки або видалення неактивних codespaces, щоб максимально використати вашу квоту.

## 1. Виконання завдань

Кожен урок матиме _необов'язкові_ завдання, які можуть бути надані однією або кількома мовами програмування, включаючи: Python, .NET/C#, Java та JavaScript/TypeScript. Цей розділ надає загальні вказівки щодо виконання цих завдань.

### 1.1 Завдання на Python

Завдання Python надаються або як програми (файли `.py`), або як Jupyter notebooks (файли `.ipynb`).
- Щоб запустити ноутбук, відкрийте його у Visual Studio Code, потім натисніть _Вибрати ядро_ (вгорі праворуч) і виберіть показану опцію Python 3 за замовчуванням. Тепер ви можете _Запустити все_ для виконання ноутбука.
- Щоб запустити Python-програми з командного рядка, дотримуйтесь специфічних для завдання інструкцій, щоб вибрати правильні файли та надати необхідні аргументи.

## 2. Налаштування провайдерів

Завдання налаштовані для роботи з Великими Мовними Моделями (LLM) через **Google Gemini API**. Gemini надає _хостингову кінцеву точку_ (API), до якої ми отримуємо доступ програмно за допомогою API-ключа. У цьому курсі ми використовуємо таких провайдерів:

 - [Google Gemini](https://ai.google.dev/gemini-api/docs/models) — основний провайдер курсу (моделі Gemini для генерації тексту та вбудовувань).
 - [Hugging Face](https://huggingface.co/docs/hub/index) для моделей з відкритим кодом та сервера виведення (необов'язково).

**Вам потрібно буде використовувати власний обліковий запис Google для цих вправ**. Деякі вказівки щодо реєстрації:

| Реєстрація | Вартість | API-ключ | Пісочниця | Коментарі |
|:---|:---|:---|:---|:---|
| [Google AI Studio](https://aistudio.google.com/) | [Ціни](https://ai.google.dev/gemini-api/docs/pricing) (є безкоштовний рівень) | [Отримати API-ключ](https://aistudio.google.com/app/apikey) | [Google AI Studio](https://aistudio.google.com/) | Доступні кілька моделей Gemini |
| [Hugging Face](https://huggingface.co/join) | [Ціни](https://huggingface.co/pricing) | [Токени доступу](https://huggingface.co/docs/hub/security-tokens) | [Hugging Chat](https://huggingface.co/chat/) | [Hugging Chat має обмежені моделі](https://huggingface.co/chat/models) |
| | | | | |

### 2.1. Створення файлу `.env`

Ми припускаємо, що ви вже зареєструвалися в Google AI Studio та отримали API-ключ Gemini.

Наступним кроком є налаштування ваших **локальних змінних середовища** наступним чином:

1. Знайдіть у кореневій папці файл `.env.copy`, який повинен мати такий вміст:

   ```bash
   # Google Gemini Provider
   GEMINI_API_KEY='<додайте ваш ключ Gemini API тут>'
   GEMINI_MODEL='gemini-3.8-flash' # За замовчуванням встановлено!
   GEMINI_EMBEDDING_MODEL='gemini-embedding-001' # За замовчуванням встановлено!

   ## Hugging Face
   HUGGING_FACE_API_KEY='<додайте ваш API або токен HuggingFace тут>'
   ```

2. Скопіюйте цей файл у `.env` за допомогою наведеної нижче команди. Цей файл _ігнорується git-ом_, зберігаючи секрети в безпеці.

   ```bash
   cp .env.copy .env
   ```

3. Заповніть значення (замініть заповнювачі праворуч від `=`), як описано в наступному розділі.

4. (Необов'язково) Якщо ви використовуєте GitHub Codespaces, ви можете зберегти змінні середовища як _секрети Codespaces_, пов'язані з цим репозиторієм. У такому випадку локальний файл .env не потрібен. **Ця опція працює тільки в GitHub Codespaces.** Якщо ви використовуєте Docker Desktop або локальне середовище, файл .env все одно потрібен.

### 2.2. Заповнення файлу `.env`

| Змінна | Опис |
|:---|:---|
| GEMINI_API_KEY | Ключ авторизації для Google Gemini API |
| GEMINI_MODEL | Модель для _генерації тексту_ (за замовчуванням `gemini-3.8-flash`) |
| GEMINI_EMBEDDING_MODEL | Модель для _текстових вбудовувань_ (за замовчуванням `gemini-embedding-001`) |
| HUGGING_FACE_API_KEY | Токен доступу користувача, який ви налаштували у своєму профілі Hugging Face |
| | |

### 2.3 Налаштування Gemini: Google AI Studio

1. Перейдіть до [Google AI Studio](https://aistudio.google.com/app/apikey) та увійдіть з обліковим записом Google.
2. Натисніть **Create API key** (Створити API-ключ) і виберіть або створіть проєкт Google Cloud.
3. Скопіюйте ключ і вставте його у змінну `GEMINI_API_KEY` у файлі `.env`.
4. Встановіть Python SDK: `pip install google-genai python-dotenv`

Приклад використання:

```python
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
    contents="Привіт! Поясни, що таке генеративний ШІ.",
)
print(response.text)
```

Не публікуйте і не діліться ключем публічно. **Не забудьте зберегти файл .env після завершення**.

### 2.4 Налаштування Hugging Face: З Профілю

Ваш токен Hugging Face можна знайти у вашому профілі в розділі [Токени доступу](https://huggingface.co/settings/tokens). Не публікуйте і не діліться ними публічно. Замість цього створіть новий токен для використання в цьому проекті та скопіюйте його у файл `.env` у змінну `HUGGING_FACE_API_KEY`. _Примітка:_ Технічно це не API-ключ, але він використовується для автентифікації, тому ми зберігаємо цю схему іменування для послідовності.