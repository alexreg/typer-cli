import subprocess


def test_script_help():
    result = subprocess.run(
        ["coverage", "run", "-m", "typer_cloup_cli", "--version"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Typer CLI version:" in result.stdout
