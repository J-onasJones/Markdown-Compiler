import sys, os

import compiler


def main():
    if HELP:
        print('''
        Usage: python markdown-compiler.py [options]
        Options:
            -h, --help              Show this help message and exit
            -s, --svelte            Compile to Svelte components
            -sf, --single-folders   Compile each folder as a single component
        ''')
        exit(0)
    
    # check if sys.argv[1] is a file or a folder
    if len(sys.argv) > 2:
        if os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]) or os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]):
            # compile all files in the folder
            compiler.markdown_to_html(sys.argv[1], sys.argv[2], TO_SVELTE)
        else:
            print('Error: Invalid file(s) or folder(s).')
            exit(1)
    else:
        print('Error: Invalid number of arguments.')
        exit(1)











if __name__ == '__main__':
    TO_SVELTE = True if '-s' in sys.argv or '--svelte' in sys.argv  else False
    HELP = True if '-h' in sys.argv or '--help' in sys.argv else False
    main()