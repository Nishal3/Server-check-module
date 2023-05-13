import click
import json
import sys

@click.command()
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None, multiple=True)
def cli(filename, server):
    if not filename or not server:
        raise click.UsageError("You must provide servers or a JSON file")

    servers = set()

    if filename:
        try:
            with open(filename, "r") as f:
                json_servers = json.load(f)
                for s in f:
                    servers.add(s)

        except:
            print(f"Error: Unable to read or open JSON file: {filename}")
            sys.exit(1)
        
        if server:
            for s in server:
                servers.add(s)
        
        print(f"servers: {servers}")


if __name__ == "__main__":
    cli()
