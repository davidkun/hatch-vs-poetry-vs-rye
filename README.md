# Comparing Hatch, Poetry, Rye, and uv

> [!NOTE]
> Originally this compared hatch, poetry, and rye, but `uv` [recently announced](https://astral.sh/blog/uv-unified-python-packaging) their release of a package manager too. So `uv` was added to the comparison here. Going forward, Astral will take stewardship of `rye` (see this [announcement](https://github.com/astral-sh/rye/discussions/659) and this [blog post](https://lucumr.pocoo.org/2024/2/15/rye-grows-with-uv/)) and it will kinda get "merged" into `uv`. The tl;dr is you should choose `uv` for your project management tool.

Each subdirectory has a Python project example for
[Hatch](https://hatch.pypa.io/latest/),
[Rye](https://rye.astral.sh),
[Poetry](https://python-poetry.org/), and
[uv](https://docs.astral.sh/uv/).

<table>
<tr>
<th>Hatch</th><th>Rye</th><th>Poetry</th>
</tr>
<tr>
<td><a href="https://hatch.pypa.io"><img src="https://hatch.pypa.io/latest/assets/images/logo.svg" height="64px" alt="Hatch"></a></td>
<td><a href="https://rye.astral.sh"><img src="https://rye.astral.sh/static/logo.svg" height="64px" alt="Rye"></a></td>
<td><a href="https://python-poetry.org"><img src="https://python-poetry.org/images/logo-origami.svg" height="64px" alt="Poetry"></a></td>
<td><a href="https://docs.astral.sh/uv"><img src="https://docs.astral.sh/uv/assets/logo-letter.svg" height="64px" alt="uv"></a></td>
</tr>
</table>


The READMEs contain step-by-step instructions for dev setup, creating the
project, adding dependencies, running tests, and adding GitHub workflow
actions:

* [hatch-demo](./hatch-demo/README.md)
* [poetry-demo](./poetry-demo/README.md)
* [rye-demo](./rye-demo/README.md)
* [uv-demo](./uv-demo/README.md)

There is a GitHub Action for each sub-project in [workflows](.github/workflows/).
Note that the actions are minimal examples for the sake of keeping things simple
(no caching, sys/env matrix, coverage, etc.).
