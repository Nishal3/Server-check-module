# servercheck

A simple CLI server checking tool

## Installation
``` Bash
$ pip install servercheck
```

## Usage

You can use servercheck to check whether or not your servers have access to other servers in the internal system. You can pass in the servers directly by using the `-s` option, here's what it would look like:

``` bash
$ servercheck -s IP1:port -s IP2:port -s IP3:port
Successful Connections
----------------------
IP1:port
IP2:port

Failed Connections
------------------
IP3:port
```

It can also be used with a JSON file with the `-f` option:

``` bash
$ servercheck -f servers.json
Successful Connections
----------------------
IP1:PORT1
IP1:PORT2
Failed Connections
------------------
IP1:PORT3
IP2:PORT1
```

Here's what a JSON file that could be passed in as a argument looks like:
``` JSON
[
    "IP1:PORT1",
    "IP1:PORT2"
    "IP1:PORT3",
    "IP2:PORT1"
]
```

You can also have it output the values as a JSON file, with the `-j` option. Here's what that would look like and what it would output.
``` bash
$ servercheck -f servers.json -j output.json
... Done!

$ cat output.json
{
    "success": [
        "IP1:PORT1",
        "IP1:PORT2"
    ],
    "failure": [
        "IP1:PORT3",
        "IP2:PORT1"
    ]
}
```

## Development

To use `servercheck` you'll need to have Python >= 3.7 and [`pipenv`][1] installed. You can then activate a virtualenv for the project and get the dependencies via these commands:

``` bash
$ pipenv install --dev
...
```

And then activate the virtual env to get it working:
``` bash
$ pipenv shell
...
(servercheck) $
```




[1]:https://docs.pipenv.org/en/latest/ "Download PIPENV"
