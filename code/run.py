import sys
sys.path.append("..")
import os
import pybank_gui

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'code'))
sys.path.insert(0, project_root)

import pybank_gui
import pybank_db

def main():
    pybank_gui.run() 

if __name__ == "__main__":
    main()