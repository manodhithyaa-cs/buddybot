## BuddyBot Backend

Local development:

1) Create and activate a virtual environment
   - Windows PowerShell:
     - `py -3 -m venv .venv`
     - `.venv\\Scripts\\Activate.ps1`

2) Install dependencies
   - `pip install -r requirements.txt`

3) Set environment variables
   - `setx OPENWEATHER_API_KEY "YOUR_KEY_HERE"`
   - Optionally set CORS origin:
     - `setx ALLOWED_ORIGIN "http://localhost:3000"`

4) Run the server
   - `python -m backend.app`
   - Server runs on `http://localhost:8000`

Endpoints:
- `GET /health`
- `POST /chat` body: `{ "message": "hello" }`
- `GET /feature/weather?city=London`
- `GET /feature/joke`
- `POST /feature/reminder` body: `{ "text": "buy milk", "delay_seconds": 60 }`

Deploy hints:
- Set `PORT` from your platform (Railway/Render) and the app will bind automatically.


