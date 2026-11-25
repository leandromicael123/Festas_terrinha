import os
from pathlib import Path
from tempfile import NamedTemporaryFile

from django.core.management.utils import get_random_secret_key


def development_key(directory):
    """Keep local sessions valid across restarts, including simultaneous first starts."""
    target = directory / ".django-secret"
    if not target.exists():
        with NamedTemporaryFile(dir=directory, prefix=".django-secret-", delete=False) as tmp:
            tmp.write(get_random_secret_key().encode())
        try:
            os.link(tmp.name, target)
        except FileExistsError:
            pass
        finally:
            Path(tmp.name).unlink()
    return target.read_text().strip()
