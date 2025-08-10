from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import List


@dataclass
class Settings:
    """Application settings sourced from environment variables.

    Defaults are suitable for local development.
    """

    openweather_api_key: str = field(default_factory=lambda: os.getenv("OPENWEATHER_API_KEY", ""))
    allowed_origins: List[str] = field(
        default_factory=lambda: [
            os.getenv("ALLOWED_ORIGIN", "http://localhost:3000"),
            os.getenv("ALLOWED_ORIGIN_ALT", "http://127.0.0.1:3000"),
        ]
    )
    port: int = int(os.getenv("PORT", "8000"))


