import typer

app = typer.Typer(help="Threat-Driven Security Test Generation for CI/CD pipelines.")


@app.command()
def version():
    """
    Show the current version of td-secgen.
    """
    typer.echo("td-secgen version 0.0.1-dev")


@app.command()
def init():
    """
    Initialize td-secgen in the current repository.

    TODO:
    - Detect CI/CD configuration
    - Generate a baseline threat model
    - Scaffold security test definitions
    """
    typer.echo("td-secgen init: not implemented yet (stub).")


def main():
    app()


if __name__ == "__main__":
    main()
