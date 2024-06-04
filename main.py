from highlighter.highlighter import Highlighter

def main():
    # Extract tokens from txt
    tokens = [
        {"data": "# Función para escapar caracteres HTML", "type": "comment"},
        {"data": "", "type": "end-line"},
        {"data": "def", "type": "reserved-word"},
        {"data": "addNums", "type": "function"},
        {"data": "()", "type": "delimiter"},
        {"data": ":", "type": "delimiter"},
        {"data": "", "type": "end-line"},
        {"data": "", "type": "tab"},
        {"data": "variable", "type": "variable"},
        {"data": "=", "type": "operator"},
        {"data": "120", "type": "literal"},
        {"data": "", "type": "end-line"},
        {"data": "", "type": "tab"},
        {"data": "variable", "type": "variable"},
        {"data": "=", "type": "operator"},
        {"data": "string", "type": "string"},
        {"data": "", "type": "end-line"},
        {"data": "", "type": "tab"},
        {"data": "if", "type": "control"},
        {"data": "(", "type": "delimiter"},
        {"data": "variable", "type": "variable"},
        {"data": "==", "type": "operator"},
        {"data": "string", "type": "string"},
        {"data": ")", "type": "delimiter"},
        
    ]

    # Highlight in html
    highlight = Highlighter()
    highlight.start_doc()

    for token in tokens:
        highlight.add_data(token["data"], token["type"])

    highlight.end_doc()


if __name__ == '__main__':
    main()

    

