clf - Command line tool to search snippets on Commandlinefu.com
===============================================================

.. image:: https://travis-ci.org/ncrocfer/clf.svg?branch=master
    :target: https://travis-ci.org/ncrocfer/clf


`Commandlinefu.com <http://www.commandlinefu.com/>`_ is the place to record awesome command-line snippets. This tool allows you to search and view the results into your terminal.

**Example 1**

.. code-block:: shell

    $ clf python server

      # python smtp server
      python -m smtpd -n -c DebuggingServer localhost:1025

      # Python version 3: Serve current directory tree at http://$HOSTNAME:8000/
      python -m http.server

      # Start a HTTP server which serves Python docs
      pydoc -p 8888 & gnome-open http://localhost:8888

      # put current directory in LAN quickly
      python -m SimpleHTTPServer

**Example 2**

.. code-block:: shell

    $ clf recursive line count

      # Recursive Line Count
      find ./ -not -type d | xargs wc -l | cut -c 1-8 | awk '{total += $1} END {print total}'

      # Recursive Line Count
      find * -type f -not -name ".*" | xargs wc -l

      # Get Total Line Count Of All Files In Subdirectory (Recursive)
      find . -type f -name "*.*" -exec cat {} > totalLines 2> /dev/null \; && wc -l totalLines && rm totalLines

      # Recursive Line Count
      wc -l `find . -name *.php`

Installation
------------

The tool works with Python 2 and Python 3. It can be installed with `Pip` :

::

    pip install clf

Usage
-----

::

    Command line tool to search snippets on Commandlinefu.com

    Usage:
      clf [options]
      clf <command> [options]
      clf <keyword> <keyword>... [options]
    
    Options:
      -h, --help      Show this help.
      -v, --version   Show version.
      -c, --color     Enable colorized output.
      -i, --id        Show the snippets id.
      -n NUMBER       Show the n first snippets [default: 25].
      --order=ORDER   The order output (votes|date) [default: votes].
      --proxy=PROXY   The proxy used to perform requests.
    
    Examples:
      clf tar
      clf python server
      clf tar --proxy=http://127.0.0.1:8080
      clf --order=date -n 3

Notes
-----

**Enable the colorized output**

You can set the :code:`CLF_COLOR` environment variable to enable the colorized output by default :

::

    $ export CLF_COLOR=1

**Use clf in your scripts**

You can import the :code:`clf` module and use it in your own scripts :

.. code-block:: python

    #!/usr/bin/env python

    from clf import Clf

    c = Clf()
    for cmd in c.browse():
        print("#{}\n{}\n".format(
            cmd.summary,
            cmd.command
        ))
