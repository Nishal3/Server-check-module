import click
import json
import sys
from typing import TextIO

from .http import ping_servers


@click.command()
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None, multiple=True)
@click.option("--json-file", "-j", default=None)
def cli(filename, server, json_file):
    output_file = None
    if json_file:
        try:
            output_file = open(json_file, "w")
        except:
            print(f"Could not open file: {json_file}")
            sys.exit(1)

    if not filename and not server:
        raise click.UsageError("You must provide servers or a JSON file")

    servers = set()

    if filename:
        try:
            with open(filename, "r") as f:
                json_servers = json.load(f)
                for s in json_servers:
                    servers.add(s)

        except:
            print(f"Error: Unable to read or open JSON file: {filename}")
            sys.exit(1)

    if server:
        for s in server:
            servers.add(s)

    results = ping_servers(servers)

    print(servers)
    show_output(results, output_file)


def show_output(results, output_file: TextIO):
    if output_file:
        print("Writing to a JSON file...")
        json.dump(results, output_file)
        output_file.close()
        print("... Done!")

    else:
        print("Successful Connections\n" "----------------------")
        for i in results["success"]:
            print(i)
        print()

        print("Failed Connections\n" "------------------")
        for i in results["failure"]:
            print(i)
        print()
