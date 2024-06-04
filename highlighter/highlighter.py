
class Highlighter:
    
    def __init__(self):
        self.file = open("output.html", "w")
    
    def start_doc(self):
        self.file.write("<html>\n")
        self.file.write("<head>\n   <link rel='stylesheet' type='text/css' href='highlighter/styles.css'>\n<head>\n\n")
        self.file.write("\n<body>\n")

    def end_doc(self):
        self.file.write("</body>\n</html>")
        self.file.close()

    def add_data(self, data, type):
        if type == "new-line":
            self.file.write("<br>\n")
        elif type == "tab":
            self.file.write("   &nbsp;&nbsp;&nbsp;&nbsp;\n")
        elif type == "space":
            self.file.write("   &nbsp;\n")
        elif type == "string":
            self.file.write(f'  <div class="{type}">"{data}"</div>\n')
        else:
            self.file.write(f'  <div class="{type}">{data}</div>\n')
