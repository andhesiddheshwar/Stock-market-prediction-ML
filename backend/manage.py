#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
from pathlib import Path


def _ensure_project_python():
    project_python = Path(__file__).resolve().parent / 'Python313' / 'python.exe'
    if not project_python.exists():
        return

    current_python = Path(sys.executable).resolve()
    if current_python == project_python.resolve():
        return

    # Re-run with the bundled interpreter so Django uses the project's installed dependencies.
    completed = subprocess.run([str(project_python), __file__, *sys.argv[1:]])
    raise SystemExit(completed.returncode)


def main():
    """Run administrative tasks."""
    _ensure_project_python()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
