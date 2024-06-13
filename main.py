from highlighter.highlighter import Highlighter
from token_separator.token_separator import TokenSeparator
import threading
import multiprocessing
import time
import os

def get_all_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def get_ext(file_path):
    ext = os.path.splitext(file_path)[-1]
    if ext[0] == ".":
        return ext[1:]
    return ext

def remove_invalid_exts(file_paths, valid):
    ret = []

    for file in file_paths:
        file_ext = get_ext(file)

        if file_ext in valid:
            ret.append(file)

    return ret

def remove_extension(file_path):
    return os.path.splitext(file_path)[0]

def highlighter(path):
    
    token = TokenSeparator(types_path="types.txt", process_file=path).run()
    # Path without extension
    html_output = remove_extension(path) + "_" + get_ext(path) + ".html"

    highlight = Highlighter(html_output)
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


def main(method):
    start_time = time.time()
    valid = ["cpp", "py", "txt"]
    process_files = get_all_files('./tests')
    process_files = remove_invalid_exts(process_files, valid)
    
    if method == "threads":
        threads = []
        for file in process_files:
            # print(file)
        # continue
            t1 = threading.Thread(target=highlighter, args=(file,))
            t1.start()
            threads.append(t1)

        for thread in threads:
            thread.join()
            
    elif method == "sequential":
        for file in process_files:
            highlighter(file)
            
    elif method == "multiprocessing":
        jobs = []
        for file in process_files:
            p = multiprocessing.Process(target=highlighter, args=(file,))
            jobs.append(p)
            p.start()

        for job in jobs:
            job.join()

    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time
    

if __name__ == "__main__":
    repeticiones = 10

    
    methods = ["multiprocessing", "sequential", "threads"]
    
    print("Ejecutando pruebas con", repeticiones, "repeticiones")
    
    for method in methods:
        promedio = 0
        print("Ejecutando con", method)
        for i in range(repeticiones):
            promedio += main(method)
        print("Promedio:", promedio / repeticiones)
        print()
    