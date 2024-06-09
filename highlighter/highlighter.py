STYLE = """
.type {
    color: #0000FF;
    display: inline;
}

body {
    background: #1c1c1c;
    font-family: 'Courier New', Courier, monospaces;
}

/* p {
    display: inline;
} */

.reserved-word{
    color: #4A9CD6;
    display: inline;
}

.comment {
    color: #84B371;
    display: inline;
}

.operator {
    color: #fff;
    display: inline;
}

.literal{
    color: #a9cbea;
    display: inline;
}

.string{
    color: rgb(209, 132, 31);
    display: inline;
}

.function{
    color: #DCDCAA;
    display: inline;
}

.delimiter{
    color: #EDDA61;
    display: inline;
}

.variable {
    color: rgb(82, 189, 199);
    display: inline;
}

.control{
    color: #ea7ae6;
    display: inline;
}
"""
class Highlighter:
    
    def __init__(self, output_path):
        self.file = open(output_path, "w")
    
    def start_doc(self):
        self.file.write("<html>\n")
        self.file.write(f"<style>\n{STYLE}\n</style>\n\n")
        self.file.write("\n<body>\n")

    def end_doc(self):
        self.file.write("</body>\n</html>")
        self.file.close()

    def add_data(self, data, type):
        data = data.replace("<", "&lt;")
        data = data.replace(">", "&gt;")

        if type == "new-line":
            self.file.write("<br>\n")
        elif type == "tab":
            self.file.write("&nbsp;&nbsp;&nbsp;&nbsp;\n")
        elif type == "space":
            self.file.write("&nbsp;")
        else:
            self.file.write(f'  <div class="{type}">{data}</div>\n')
