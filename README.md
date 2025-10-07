# Zodiac — Horoscope demo

Small demo that fetches daily horoscopes from an external API and exposes a minimal web UI.

This repository contains a tiny Flask app that calls an external horoscope API and renders the prediction on a simple page.

## Features

- Thin API client to call the horoscope endpoint
- Minimal Flask UI to request and display results
- Configurable via environment variables (`.env`) for local development
- Styles moved to `static/css/style.css` (dark blue + gold theme)

## Quick start (local)

Prerequisites:
- Python 3.10+ (or 3.8+)
- git (optional)

1. Create virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Prepare environment variables:

- Copy `.env.example` to `.env` and fill `ZODIAC_API_KEY` with your key.

```bash
cp .env.example .env
# then edit .env and set ZODIAC_API_KEY
```

4. Run the app:

```bash
python3 app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Files of interest
- `api_client.py` — small wrapper that calls the external API
- `config.py` — centralizes API URL, API key and defaults (reads from env)
- `app.py` — Flask app and routes
- `templates/index.html` — Jinja2 template for the UI
- `static/css/style.css` — CSS theme (dark blue + gold)

## Environment variables
See `.env.example`. Important ones:
- `ZODIAC_API_KEY` — your API key (keep secret)
- `ZODIAC_API_URL` — base API url (optional)
- `ZODIAC_TIMEOUT_SECONDS` — request timeout in seconds
- `SECRET_KEY` — Flask secret key (optional)


