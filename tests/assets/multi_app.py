import typer_cloup as typer

sub_app = typer.Typer()

variable = "Some text"


@sub_app.command()
def hello(name: str = "World", age: int = typer.Option(0, help="The age of the user")):
    """
    Say hello
    """
    typer.echo(f"Hello {name}")


@sub_app.command()
def hi(user: str = typer.Argument("World", help="The name of the user to greet")):
    """
    Say hi
    """
    pass  # pragma: no cover


@sub_app.command()
def bye():
    """
    Say bye
    """
    typer.echo("sub bye")


app = typer.Typer(help="Demo App", epilog="The end")
app.add_sub(sub_app, name="sub")


@app.command()
def top():
    """
    Top command
    """
    typer.echo("top")
