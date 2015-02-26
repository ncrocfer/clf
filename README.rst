clf - Command line tool to search snippets on Commandlinefu.com
===============================================================

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

      # An alternative to: python -m SimpleHTTPServer for Arch Linux
      python3 -m http.server

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
      clf --browse [options]
      clf <command> [options]
      clf <keyword> <keyword>... [options]

    Options:
      -h, --help     Show this help.
      -v, --version  Show version.
      -c, --color    Enable colorized output
      -b, --browse   Browse the Commandlinefu.com archive.
      --order=ORDER  The order output (votes|date) [default: votes]

    Examples:
      clf tar
      clf python server
      clf --browse --order=date

Notes
-----

- You can set the CLF_COLOR environment variable to enable the colorized output by default.

Author
------

-  Nicolas Crocfer (`@ncrocfer <http://twitter.com/ncrocfer>`_)
