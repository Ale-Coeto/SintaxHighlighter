# SintaxHighlighter
Scripts to highlight code syntax. 

Reads from input file (.txt, .py, .cpp, etc) and displays highlighted code in the output.html file.


## Structure:
The input is processed to extract tokens and their types:
Spacing:
- Space: space
- Tab: tab
- Newline: newline

Key words and characters:
- Reserved word: reserved-word
- Comments: comment
- Operators: operator
- Literals: literal
- Strings: string
- Functions: function
- Variable: variable
- Delimiter: delimiter


Tokens are then highlighted with the following colors: 

|  Token         |   Keyword        |  Color           | HexCode |
|----------------|------------------|------------------|---------|
| Reserved word  | reserved-word    |  Blue            | #4A9CD6 |
| Comments       | comment          |  Green           | #84B371 |
| Operators      | operator         |  White           | #000000 |
| Literals       | literal          |  Light Blue      | #5EB2BE |
| Strings        | string           |  Orange          | #E2A951 |
| Functions      | function         |  Yellow          | #DCDCAA |
| Variable       | variable         |  Green           | #000000 |
| Delimiter      | delimiter        |  Dark yellow     | #FFD70A |



## Usage
To run the script, use the following command from the main directory:

```bash
python3 main.py  
```

Optionally, specify the input file name:
```bash
python3 main.py --path tests/test.py
```

    
