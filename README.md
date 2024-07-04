# Comparing Hatch, Poetry, and Rye

Each subdirectory has a Python project example for Hatch, Rye, and Poetry.

The READMEs contain step-by-step instructions for dev setup, creating the
project, adding dependencies, running tests, and adding GitHub workflow
actions:

* [hatch-demo](./hatch-demo/README.md)
* [poetry-demo](./poetry-demo/README.md)
* [rye-demo](./rye-demo/README.md)

There is a GitHub Action for each sub-project in [workflows](.github/workflows/).
Note that the actions are minimal examples for the sake of keeping things simple
(no caching, sys/env matrix, coverage, etc.).
