#!/usr/bin/env python2
"""UGTrain-GUI is a desktop application to manage UGTrain config files.
Author: Morteza Nourelahi Alamdari (Mortezaipo)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from general import General


class Main:
    def __init__(self):
        self.general = General()
        self.general.draw_gui()

if __name__ == "__main__":
    Main()
