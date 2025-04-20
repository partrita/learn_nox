import nox
import sys
import re
import tomllib

# === Extract Python version from pyproject.toml ===
try:
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
        version_spec = pyproject["project"]["requires-python"]
except (FileNotFoundError, KeyError, tomllib.TOMLDecodeError) as e:
    print(f"Failed to parse pyproject.toml: {e}", file=sys.stderr)
    sys.exit(1)

match = re.search(r"[>=~=]\s*(\d+\.\d+)", version_spec)
if not match:
    print(f"Could not extract Python version from: {version_spec}", file=sys.stderr)
    sys.exit(1)

PYTHON_VERSION = match.group(1)  # e.g., "3.13"
CODE_DIR = "app/"
TEST_DIR = "tests/"
DEV_GROUP = "dev"

# Use uv to manage the virtual environment for all sessions
nox.options.default_venv_backend = "uv"

@nox.session(python=PYTHON_VERSION)
def lint(session: nox.Session) -> None:
    """
    Run Ruff to lint and check formatting of source files.

    This session installs only the linting group and runs two Ruff commands:
    - ruff check: validate lint rules
    - ruff format --check: verify formatting, do not modify
    """
    session.run(
        "uv", "sync", "--group", DEV_GROUP,
        f"--python={session.python}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
        external=True
    )

    session.run("ruff", "check", CODE_DIR)
    session.run("ruff", "format", "--check", CODE_DIR)
    
@nox.session(python=PYTHON_VERSION)
def tests(session):
    session.run(
        "uv", "sync", "--group", DEV_GROUP,
        f"--python={session.python}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
        external=True
    )
    session.run("pytest")

