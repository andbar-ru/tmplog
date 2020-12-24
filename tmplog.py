import inspect
import os
from pprint import pformat


FILE = '/tmp/log.txt'


def tmplog(*args, file=None, context='nlf', format_value=True, **kwargs):
    """Logs to file for debugging purposes.
    Values to be logged are passed with **kwargs.

    Args:
        file: file which write into
        context:
            if 'n' in context, log current filename;
            if 'l' and 'n' in context also log line number;
            if 'f' in context, log function name.
        format_value: format passed values with pprint.pformat
    """
    file = file or FILE

    frameinfo = inspect.stack()[1]
    filename = os.path.basename(frameinfo.filename) if 'n' in context else ''
    lineno = ':{}'.format(frameinfo.lineno) if 'l' in context and 'n' in context else ''
    function = '({})'.format(frameinfo.function) if 'f' in context else ''

    with open(file, 'a+') as f:
        output = '{}{}{}'.format(filename, lineno, function)
        if output:
            output += ': '
        output += ', '.join(pformat(v) if format_value else v for v in args)
        if output and len(kwargs.keys()) > 0:
            output += '; '
        output += ', '.join(
            '{}={}'.format(k, pformat(v) if format_value else v) for k, v in kwargs.items()
        )
        output += '\n'
        f.write(output)
