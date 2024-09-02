# uv Demo

## Steps

1. Install `uv`:
```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a new project (with the `--lib` [option](https://docs.astral.sh/uv/concepts/projects/#libraries)):
```bash
$ uv init --lib uv-demo
```

> [!TIP]
> The `--lib` option specifies the `build-system` for us in `pyproject.toml` and creates the project in the [src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).


3. Add dependencies (`requests`, `polars`, `pytest`, `ruff`)
    * Note: Add `pytest` and `ruff` under the `dev` group.

```bash
$ uv add requests
$ uv add polars
$ uv add --dev pytest
$ uv add --dev ruff
```

Those commands added the following sections to our initial `pyproject.toml` file, and created/updated a `uv.lock` file.

```toml
[project]
name = "uv-demo"
version = "0.1.0"
description = ""
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "polars>=1.6.0",
    "requests>=2.32.3",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "pytest>=8.3.2",
    "ruff>=0.6.3",
]
```

4. Add code (`demo.py`, `__init__.py`, `__main__.py`) and tests (`test_demo.py`).

5. Run tests and lint/format code:
```bash
$ uv run pytest
$ uv run ruff check --fix
$ uv run ruff format
```

6. Run the app:
```bash
$ uv run python -m uv_demo
```

Or, add the following section to `pyproject.toml`:
```toml
[project.scripts]
"uv-demo" = "uv_demo:main"
```

to run it more directly:
```bash
$ uv run uv-demo
```

9. Add [uv-based GH workflow](../.github/workflows/uv.yml) to lint and run tests.