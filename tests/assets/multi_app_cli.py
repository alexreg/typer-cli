import typer_cloup as typer

sub_app = typer.Typer()


@sub_app.command()
def hello():
    typer.echo("sub hello")


@sub_app.command()
def bye():
    typer.echo("sub bye")


cli = typer.Typer()
cli.add_sub(sub_app, name="sub")


@cli.command()
def top():
    typer.echo("top")
