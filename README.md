# Comparing Hatch, Poetry, and Rye

Each subdirectory has a Python project example for
[Hatch](https://hatch.pypa.io/latest/),
[Rye](https://rye.astral.sh), and
[Poetry](https://python-poetry.org/).

<table>
<tr>
<th>Hatch</th><th>Rye</th><th>Poetry</th>
</tr>
<tr>
<td><a href="https://hatch.pypa.io"><img src="https://hatch.pypa.io/latest/assets/images/logo.svg" height="64px" alt="Hatch"></a></td>
<td><a href="https://rye.astral.sh"><img src="https://rye.astral.sh/static/logo.svg" height="64px" alt="Rye"></a></td>
<td><a href="https://python-poetry.org"><img src="https://python-poetry.org/images/logo-origami.svg" height="64px" alt="Poetry"></a></td>
</tr>
</table>


The READMEs contain step-by-step instructions for dev setup, creating the
project, adding dependencies, running tests, and adding GitHub workflow
actions:

* [hatch-demo](./hatch-demo/README.md)
* [poetry-demo](./poetry-demo/README.md)
* [rye-demo](./rye-demo/README.md)

There is a GitHub Action for each sub-project in [workflows](.github/workflows/).
Note that the actions are minimal examples for the sake of keeping things simple
(no caching, sys/env matrix, coverage, etc.).
