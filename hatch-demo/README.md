# Hatch Demo

## Steps

1. Install `hatch`

```bash
$ pipx install hatch
# or 
$ brew install pipx
```

2. Create new project
```bash
$ hatch new "Hatch Demo"
$ cd hatch-demo
```

3. Create default environment
```bash
$ hatch env create
```

4. Set `uv` as the default installer by adding this to `pyproject.toml`:

```toml
[tool.hatch.envs.default]
installer = "uv"
```

5. Add dependencies (`requests`, `polars`, `pytest`, `ruff`)
    * Note 1: I didn't see a way to add deps via `hatch` command, so this was manually done by editing `pyproject.toml`. (This seems to be the procedure described in [their docs](https://hatch.pypa.io/dev/environment/#dependencies).)
    * Note 2: Add `pytest` and `ruff` under the `dev` environment.

```toml
[tool.hatch.envs.default]
installer = "uv"
dependencies = ["polars", "requests"]

[tool.hatch.envs.dev]
installer = "uv"
dependencies = [
  "hatch-demo",
  "pytest",
  "ruff"
]
```
_Note: You have to reference `hatch-demo` in order to get the project deps needed for running tests._

6. Add `test` and `lint` scripts to `dev` env

```toml
[tool.hatch.envs.dev.scripts]
test = "pytest"
lint = "ruff check --fix && ruff format"
```

7. Create/install the env

```bash
$ hatch env create dev
```

8. Add code (`demo.py`) and tests (`test_demo.py`)

9. Check envs

```bash
$ hatch env show
                  Standalone                  
┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Name    ┃ Type    ┃ Dependencies ┃ Scripts ┃
┡━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ default │ virtual │ polars       │ run     │
│         │         │ requests     │         │
├─────────┼─────────┼──────────────┼─────────┤
│ dev     │ virtual │ pytest       │ lint    │
│         │         │ ruff         │ run     │
│         │         │              │ test    │
└─────────┴─────────┴──────────────┴─────────┘
```

10. Run tests and lint/format code

```bash
$ hatch run dev:test
$ hatch run dev:lint
```

11. Add default script to run the app

```toml
[tool.hatch.envs.default.scripts]
run = "python src/hatch_demo/demo.py"
```

12. Run the app
```bash
$ hatch run default:run
```

## Notes

* Not sure how to install the project so that it can called like `python -m hatch_demo`
* Not sure how to call the entrypoint scripts