#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools
import pypandoc

def main():

    setuptools.setup(
        name             = "tmux-control",
        version          = "2016-08-01T1603Z",
        description      = "configure and control tmux",
        long_description = pypandoc.convert("README.md", "rst"),
        url              = "https://github.com/wdbm/tmux-control",
        author           = "Will Breaden Madden",
        author_email     = "w.bm@cern.ch",
        license          = "GPLv3",
        py_modules       = [
                           "tmux-control"
                           ],
        install_requires = [
                           "propyte"
                           ],
        scripts          = [
                           "tmux-control.py"
                           ],
        entry_points     = """
            [console_scripts]
            tmux-control = tmux-control:tmux-control
        """
    )

def read(*paths):
    with open(os.path.join(*paths), "r") as filename:
        return filename.read()

if __name__ == "__main__":
    main()
