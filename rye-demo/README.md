# Rye Demo

## Steps

1. Install `rye`:
```bash
$ curl -sSf https://rye.astral.sh/get | bash
```

2. Create a new project (with `--script` option for later):
```bash
$ rye init --script rye-demo
```

3. Add dependencies (`requests`, `polars`, `pytest`, `ruff`)
    * Note: Add `pytest` and `ruff` under the `dev` group.

```bash
$ rye add requests
$ rye add polars
$ rye add --dev pytest
$ rye add --dev ruff
```

Those commands added the following sections to our initial `pyproject.toml` file, and created/updated `requirements.lock` and `requirements-dev.lock` files.

```toml
[project]
...
dependencies = [
    "requests>=2.32.3",
    "polars>=1.0.0",
]

[tool.rye]
managed = true
dev-dependencies = [
    "pytest>=8.2.2",
    "ruff>=0.5.0",
]
```

4. Install the project?
```bash
$ rye sync
```

5. Add code (`demo.py`) and tests (`test_demo.py`).

6. Run tests and lint/format code:
```bash
$ rye run pytest
$ rye run ruff check --fix
$ rye run ruff format
```

Note: `rye` comes with formatting/linting commands (as of version `0.20.0`), so we could skip the roundabout call to `ruff` and just call:
```bash
$ rye lint --fix
$ rye fmt
```

7. Run the app:
```bash
$ rye run python -m rye_demo
# or
$ rye run rye-demo
```

9. Add [rye-based GH workflow](../.github/workflows/rye.yml) to check linting and run tests.