from highlighter.highlighter import Highlighter
from token_separator.token_separator import TokenSeparator
import argparse

def parse_args():
    '''parses the command line arguments'''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--path', type=str, default="tests/test.txt", help="path to test file")

    return parser.parse_args()


def main():
    args = parse_args()
    token = TokenSeparator(types_path="types.txt", process_file=args.path).run()

    # Highlight in html
    highlight = Highlighter()
    highlight.start_doc()

    counter = 0
    for i in range(len(token)):
        if token[i]["type"] == "space":
            counter += 1
        else:
            counter = 0
        
        if counter == 2:
            highlight.add_data("", token[i]["type"])
            counter = 0
        
        if token[i]["type"] != 'space':
            highlight.add_data(token[i]["data"], token[i]["type"])
    

    highlight.end_doc()


if __name__ == '__main__':
    main()

    

