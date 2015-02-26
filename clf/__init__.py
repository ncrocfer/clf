# -*- coding: utf-8 -*-

"""
   ________    ______
  / ____/ /   / ____/
 / /   / /   / /_
/ /___/ /___/ __/
\____/_____/_/

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
"""

from docopt import docopt
import os
from pygments import highlight
from pygments.lexers.shell import BashLexer
from pygments.formatters import TerminalFormatter

from clf.constants import VERSION, BLUE, END
from clf.api import Clf


def run():
    arguments = docopt(__doc__, version=VERSION)

    f = Clf(format="json",
            order=arguments['--order'])

    if arguments['--browse']:
        commands = f.browse()
    elif arguments['<command>']:
        commands = f.command(arguments['<command>'])
    elif arguments['<keyword>']:
        commands = f.search(arguments['<keyword>'])

    for command in commands:
        if (arguments['--color']) or (os.getenv('CLF_COLOR')):
            output = '{}# {}{}\n'.format(BLUE, command.summary, END)
            output += highlight(command.command,
                                BashLexer(),
                                TerminalFormatter(bg="dark"))
        else:
            output = '# {}\n'.format(command.summary)
            output += command.command + "\n"

        print(output)

if __name__ == '__main__':
    run()
