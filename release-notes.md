# Release Notes

## Latest Changes

* 📝 Miscellaneous improvements to docs
* ⬆️ Update dependency `pytest-xdist`
* ✏ Fix comment in `scripts/test.sh`

## 0.2.0

* ⬆ Update dependency *typer-cloup* to 0.9.0

## 0.1.0

* 👷 Fix definitions of manual inputs in GitHub workflows
* 🔧 Rename package module to `typer_cloup_cli`
* ⬆ Update dependency *typer-cloup* to 0.8.0
* 🔧 Update scripts
* ✨ Replace calls to `sys.exit()` with `raise typer.Exit()`
* ✅ Add `pragma: no cover` to line only used with old Python
* 📝 Update more docs to point to own site

## 0.0.13

* 🔧 Fix single-sourcing of package version
* ⬆ Update build system
* 📝 Add dependency *docstring_parser*
* ⬆ Update dependency *typer-cloup*
* 📝 Do not prefix calls with `python -m` when unnecessary
* 🐛 Fix Poetry set-up in GitHub workflows
* ✨ Add support for Click 8
* ✨ Migrate from *typer* to *typer-cloup*
* ⬇️ Drop support for Python 3.6
* 👷 Fix *poetry* commands in GitHub workflows
* 👷 Update versions of actions in GitHub workflows
* 👷 Fix formatting of GitHub workflows
* 📝 Update copyright in license
* 📝 Update docs to point to own site
* ✏ Fix grammar/style in README
* ✏ Fix indentation in README
* 📝 Update project metadata
* 🔧 Sort gitignore entries
* ✅ Report coverage in XML

## 0.0.12

* ✨ Move CI to GitHub Actions, remove dependency on `importlib-metadata`. This would fix use cases that also depend on `importlib-metadata` and could have conflicts, like installing `mkdocs`, as now `typer-cli` no longer depends on `importlib-metadata`. PR [#48](https://github.com/tiangolo/typer-cli/pull/48) by [@tiangolo](https://github.com/tiangolo).

## 0.0.11

* 🐛 Fix latest changes GitHub Action. PR [#34](https://github.com/tiangolo/typer-cli/pull/34) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update importlib-metadata requirement from ^1.5 to >=1.5,<3.0. PR [#29](https://github.com/tiangolo/typer-cli/pull/29).
* 👷 Add Latest Changes GitHub Action. PR [#30](https://github.com/tiangolo/typer-cli/pull/30) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update black requirement from ^19.10b0 to ^20.8b1. PR [#28](https://github.com/tiangolo/typer-cli/pull/28).
* ⬆️ Update pytest-xdist requirement from ^1.31.0 to ^2.1.0. PR [#27](https://github.com/tiangolo/typer-cli/pull/27).

## 0.0.10

* ⬆️ Update pytest requirement from ^5.4.3 to ^6.0.1. PR [#22](https://github.com/tiangolo/typer-cli/pull/22).
* Update tests with defaults. PR [#24](https://github.com/tiangolo/typer-cli/pull/24).
* Add support for *CLI Arguments* with `help`. PR [#20](https://github.com/tiangolo/typer-cli/pull/20) by [@ovezovs](https://github.com/ovezovs).
* ⬆ Upgrade Typer version to 0.3.0. PR [#13](https://github.com/tiangolo/typer-cli/pull/13).
* ⬆️ Update mypy requirement from ^0.761 to ^0.782. PR [#18](https://github.com/tiangolo/typer-cli/pull/18).
* ⬆️ Update pytest requirement from ^4.4.0 to ^5.4.3. PR [#16](https://github.com/tiangolo/typer-cli/pull/16).
* ⬆️ Update isort requirement from ^4.3.21 to ^5.0.6. PR [#15](https://github.com/tiangolo/typer-cli/pull/15).
* Update GitHub action issue-manager and add Dependabot. PR [#14](https://github.com/tiangolo/typer-cli/pull/14).

## 0.0.9

* Upgrade Typer to `0.2.1`. PR [#9](https://github.com/tiangolo/typer-cli/pull/9).

## 0.0.8

* Upgrade Typer to `0.1.1`. PR [#8](https://github.com/tiangolo/typer-cli/pull/8).

## 0.0.7

* Upgrade Typer to version 0.1.0. PR [#7](https://github.com/tiangolo/typer-cli/pull/7).

## 0.0.6

* Synchronize README with docs in [Typer - Typer CLI](https://typer.tiangolo.com/typer-cli/) and update links. PR [#5](https://github.com/tiangolo/typer-cli/pull/5).
* Upgrade **Typer** after re-implementing completion:
    * Add support for PowerShell in modern versions (e.g. Windows 10).
    * Fix support for user-provided completions.
    * Fix creation of sub-command `run` in each internal case.
    * PR [#4](https://github.com/tiangolo/typer-cli/pull/4).

## 0.0.5

* Add support for [generating Markdown docs](https://github.com/tiangolo/typer-cli#generate-docs) for **Typer** apps. PR [#3](https://github.com/tiangolo/typer-cli/pull/3).

## 0.0.4

* Handle default Typer to extract and run in this priority:
    * App object from `--app` *CLI Option*.
    * Function to convert to a **Typer** app from `--func` *CLI Option*.
    * **Typer** app in a variable with a name of `app`, `cli`, or `main`.
    * The first **Typer** app available in the file, with any name.
    * A function in a variable with a name of `main`, `cli`, or `app`.
    * The first function in the file, with any name.
    * PR [#2](https://github.com/tiangolo/typer-cli/pull/2).

## 0.0.3

* Add Travis CI. PR [#1](https://github.com/tiangolo/typer-cli/pull/1).
