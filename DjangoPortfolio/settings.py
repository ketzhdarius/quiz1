INSTALLED_APPS = [
    ...
    'projects',
]
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        ...
        'DIRS': [],
        'APP_DIRS': True,
    },
]

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
