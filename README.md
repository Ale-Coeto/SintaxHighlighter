# SintaxHighlighter
Scripts to highlight code syntax. 

## 

tokens = [
    {"data": "# Función para escapar caracteres HTML", "type": "comments"},
    {"data": "def", "type": "kw"},
    {"data": "", "type": "newline"},
    {"data": "", "type": "space"},
    {"data": "", "type": "tab"},
]


Types:
    Space: space
    Tab: tab
    Newline: newline

    Reserved word: reserved-word
    Comments: comment
    Operators: operator
    Literals: literal
    Strings: string
    Functions: function
    Variable: variable
    Delimiter: delimiter

Tabla 

|  Token         |   Keyword        |  Color           | HexCode |
|----------------|------------------|------------------|---------|
| Reserved word  | reserved-word    |  Azul            | #4A9CD6 |
| Comments       | comment          |  Verde           | #84B371 |
| Operators      | operator         |  Negro           | #000000 |
| Literals       | literal          |  Azul claro      | #5EB2BE |
| Strings        | string           |  Naranja         | #E2A951 |
| Functions      | function         |  Amarillo        | #DCDCAA |
| Variable       | variable         |  Negro           | #000000 |
| Delimiter      | delimiter        |  Amarillo fuerte | #FFD70A |

