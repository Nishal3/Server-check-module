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

It can also be used with a JSON file with the `-r` option:

``` bash
$ servercheck -r servers.json
Successful Connections
----------------------
IP1:port
IP2:port

Failed Connections
------------------
IP3:port
```

Here's what a JSON file that could be passed in as a argument looks like:
``` JSON
[
    "JSONIP:PORT",
    "JSONIP:PORT",
    "JSONIP2:PORT2"
]
```

## Development

To use `servercheck` you'll need to have Python >= 3.7 and [`pipenv`][1] installed. You can then activate a virtualenv for the project and get the dependencies by these commands:

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
