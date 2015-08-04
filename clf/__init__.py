# -*- coding: utf-8 -*-

"""
   ________    ______
  / ____/ /   / ____/
 / /   / /   / /_
/ /___/ /___/ __/
\____/_____/_/

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
  -l, --local     Read the local snippets.
  -s ID           Save the snippet locally.
  -n NUMBER       Show the n first snippets [default: 25].
  --order=ORDER   The order output (votes|date) [default: votes].
  --proxy=PROXY   The proxy used to perform requests.

Examples:
  clf tar
  clf python server
  clf tar --proxy=http://127.0.0.1:8080
  clf --order=date -n 3
"""

from docopt import docopt
import os
from pygments import highlight
from pygments.lexers.shell import BashLexer
from pygments.formatters import TerminalFormatter

from clf.constants import VERSION, BLUE, END
from clf.api import Clf
from clf.utils import save_snippet, get_local_snippets
from clf.exceptions import RequestsException, OSException, DuplicateException

__all__ = ['Clf']


def run():
    arguments = docopt(__doc__, version=VERSION)

    f = Clf(format="json",
            order=arguments['--order'],
            proxy=arguments['--proxy'])

    # Save the snippet locally
    if arguments['-s']:
        try:
            snippet = save_snippet(arguments['-s'], f._get_proxies())
        except(RequestsException, OSException, DuplicateException) as e:
            print(e)
        else:
            print("The snippet has been successfully saved.")
        exit()

    # Retrieve the snippets list
    if arguments['--local']:
        commands = get_local_snippets()
    elif arguments['<command>']:
        commands = f.command(arguments['<command>'])
    elif arguments['<keyword>']:
        commands = f.search(arguments['<keyword>'])
    else:
        commands = f.browse()

    # Show the snippets id
    if arguments['--id']:
        sid = lambda c: '({})'.format(c.id)
    else:
        sid = lambda c: ''

    # Display in colors
    if (arguments['--color']) or (os.getenv('CLF_COLOR')):
        def get_output(command):
            detail = highlight(command.command,
                               BashLexer(), TerminalFormatter(bg="dark"))
            return '{}#{} {}{}\n{}'.format(BLUE, sid(command),
                                           command.summary, END, detail)
    else:
        def get_output(command):
            return '#{} {}\n{}\n'.format(sid(command),
                                         command.summary, command.command)

    # Limit the number of snippets
    try:
        limit = int(arguments['-n'])
    except ValueError:
        limit = 25

    # Display the snippets
    for idx, command in enumerate(commands):
        if limit == idx:
            break

        print(get_output(command))

if __name__ == '__main__':
    run()
