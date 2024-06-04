import re

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def is_valid_python_name(name):
    if not name or not (name[0].isalpha() or name[0] == '_'):
        return False

    for char in name[1:]:
        if not (char.isalnum() or char == '_'):
            return False

    return True

class TokenSeparator:
    class TokenTypes:
        RESERVED = "reserved-word"
        COMMENTS = "comment"
        SPACE = "space"
        TAB = "tab"
        NEWLINE = "new-line"
        OPERATORS = "operator"
        LITERALS = "literal"
        STRINGS = "string"
        FUNCTIONS = "function"
        VARIABLES = "variable"
        DELIMITERS = "delimiter"
        UNKNOWN = "unknown"
        CONTROL = "control"

    class States:
        READING = "READING"
        COMMENT = "COMMENT"
        STRING = "STRING"

    def __init__(self, types_path, process_file) -> None:
        self.current_token = ""
        self.state = self.States.READING
        self.tokens = []
        self.load_file(process_file)
        self.read_lexical_categories(types_path)

    # Función para cargar las categorías léxicas desde un archivo
    def read_lexical_categories(self, file):
        categories = {}
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    key, value = line.split('=', 1)
                    categories[key.strip()] = value.strip().split('|')
        self.categories = categories

    def load_file(self, process_file):
        self.process_lines = []
        with open(process_file, 'r', encoding='utf-8') as f:
            for line in f:
                self.process_lines.append(line.rstrip())

    def predict_token(self, token):
        if token in self.categories["comments"]:
            return self.TokenTypes.COMMENTS
        elif token in self.categories["operators"]:
            return self.TokenTypes.OPERATORS
        elif token in self.categories["reserved_words"]:
            return self.TokenTypes.RESERVED
        elif token in self.categories["control"]:
            return self.TokenTypes.CONTROL
        elif token in self.categories["delimiters"]:
            return self.TokenTypes.DELIMITERS
        elif is_int(token) or is_float(token):
            return self.TokenTypes.LITERALS
        elif is_valid_python_name(token):
            return self.TokenTypes.VARIABLES
        elif token in [" "]:
            return self.TokenTypes.SPACE
        elif token in ["\t"]:
            return self.TokenTypes.TAB

        return self.TokenTypes.UNKNOWN
    
    def stop_reading(self, character):
        if character in [" ", "\t"]:
            return True
        elif character in self.categories["comments"]:
            return True
        elif character in self.categories["delimiters"]:
            return True
        elif character in self.categories["operators"]:
            return True
        
        return False

    def add_predicted_token(self, token):
        predicted = self.predict_token(token)
        if predicted != self.TokenTypes.UNKNOWN:
            self.tokens.append({"data": token, "type": predicted})

    def process_line(self):
        self.current_state = self.States.READING
    
        self.current_token = ""
        line = self.process_lines[self.line_index]
        self.line_index += 1

        for i in range(len(line)):
            self.process_character(line[i])

        if self.current_state == self.States.COMMENT:
            self.tokens.append({"data": self.current_token, "type": self.TokenTypes.COMMENTS})
        elif self.current_state == self.States.READING:
            self.add_predicted_token(self.current_token)

        self.tokens.append({"data": "", "type": self.TokenTypes.NEWLINE})
        

    def process_character(self, character):
        # print(self.current_token)
        if self.current_state == self.States.COMMENT:
            self.current_token += character
        elif self.current_state == self.States.STRING:
            if character in ['"', "'"]:
                self.current_token += character
                self.tokens.append({"data": self.current_token, "type": self.TokenTypes.STRINGS})
                self.current_token = ""
                self.current_state = self.States.READING
            else:
                self.current_token += character
        else:
            if character in self.categories["comments"]:
                    self.add_predicted_token(self.current_token)
                    self.current_token = character
                    self.current_state = self.States.COMMENT
            elif self.stop_reading(character):
                self.add_predicted_token(self.current_token)
                self.current_token = character
                self.add_predicted_token(self.current_token)
                self.current_token = ""
            else:
                if character in ['"', "'"]:
                    self.current_state = self.States.STRING
                    self.add_predicted_token(self.current_token)
                    self.current_token = character
                else:
                    self.current_token += character

    def post_process(self):
        token_count = len(self.tokens)

        for i in range(token_count):
            if i +1 < token_count and self.tokens[i]["type"] == self.TokenTypes.VARIABLES and self.tokens[i + 1]["data"] == "(":
                self.tokens[i]["type"] = self.TokenTypes.FUNCTIONS

    def run(self):
        self.line_index = 0

        while self.line_index < len(self.process_lines):
            self.process_line()

        self.post_process()
        return self.tokens
    
   