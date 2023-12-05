#!/usr/bin/env python3

from glob import glob
import os 
import subprocess



def repair(input_filename):
    print('# repairing ' + input_filename)
    path = os.path.dirname(input_filename)
    output_filename = os.path.join(path, 'tmp.html')
    output_file = open(output_filename, 'w')
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if '<title>' not in line:
                output_file.write(line)
            else:
                output_file.write(line)
                output_file.write('    <script src="../_static/plotly-2.27.0.min.js"></script>')
    output_file.close()
    command = f'mv {output_filename} {input_filename}'
    print('...' + command)
    subprocess.call(command, shell=True)
            

def main():
    current_directory = os.getcwd()
    file_list_total = glob(current_directory + '/doc/_build/html/**/*.html', recursive=True)
    for filename in file_list_total:
        repair(filename)

           





if __name__ == "__main__":
    main() 
    