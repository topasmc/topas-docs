from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ['TopasLexer']


class TopasLexer(RegexLexer):

    name = 'TOPAS'
    aliases = ['topas']
    filenames = ['*.txt']

    tokens = {
        'root': [
            (r'#.*$', Comment),
            (r'(?i)(includefile|inheritedvalue)', Keyword.Namespace),
            (r'^([bidus]v?)(:)', bygroups(Keyword.Type, Text)),
            (r'(?i)(ma|el|is|ge|gr|ph|so|sc|tf|ts|vr)([/\w]*/)([\w]+)',
                bygroups(Name.Class, Name.Class, Name.Variable)),
            (r'"(?i)(true|false|t|f|1|0)"', Keyword.Constant),
            (r'"', String, 'string'),
            (r'(?<!\w)[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', Number),
            (r'[=+*-]', Operator),
            (r'.', Text),
        ],
        'string': [
            ('[^"]+', String),
            ('"', String, '#pop'),
        ]
    }
