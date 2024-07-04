# Poetry Demo

## Steps

1. Install `poetry`:

```bash
$ pipx install poetry
# or
$ brew install poetry
```

2. Create new project (with [src-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)):
```bash
$ poetry new --src poetry-demo
```

3. Add dependencies (`requests`, `polars`, `pytest`, `ruff`)
    * Note: Add `pytest` and `ruff` under the `dev` group.

```bash
$ poetry add requests
$ poetry add polars
$ poetry add pytest --group dev
$ poetry add ruff --group dev
```

Those commands added the following sections to our initial `pyproject.toml` file, and created/updated a `poetry.lock` file.

```toml
[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.32.3"
polars = "^1.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^8.2.2"
ruff = "^0.5.0"
```

4. Install the project:
```bash
$ poetry install
```

5. Add code (`demo.py`) and tests (`test_demo.py`).

6. Run tests and lint/format code:
```bash
$ poetry run pytest
$ poetry run ruff check --fix
$ poetry run ruff format
```

7. Add entrypoint script to run the app:
```toml
[tool.poetry.scripts]
rundemo = 'poetry_demo.demo:main'
```

8. Run the app:
```bash
$ rundemo

shape: (3, 5)
┌────────────┬──────────────┬─────────────┬──────────────┬─────────────┐
│ species    ┆ sepal_length ┆ sepal_width ┆ petal_length ┆ petal_width │
│ ---        ┆ ---          ┆ ---         ┆ ---          ┆ ---         │
│ str        ┆ f64          ┆ f64         ┆ f64          ┆ f64         │
╞════════════╪══════════════╪═════════════╪══════════════╪═════════════╡
│ setosa     ┆ 116.9        ┆ 81.7        ┆ 33.2         ┆ 6.1         │
│ virginica  ┆ 324.5        ┆ 146.2       ┆ 273.1        ┆ 99.6        │
│ versicolor ┆ 281.9        ┆ 131.8       ┆ 202.9        ┆ 63.3        │
└────────────┴──────────────┴─────────────┴──────────────┴─────────────┘
```

9. Add [poetry-based GH workflow](../.github/workflows/poetry.yml) to check linting and run tests.