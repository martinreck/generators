#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Java Examples Compiler
Copyright (C) 2012-2013 Matthias Bolte <matthias@tinkerforge.com>

compile_java_examples.py: Compile all examples for the Java bindings

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

import sys
import os
import subprocess

sys.path.append(os.path.split(os.getcwd())[0])
import common

class JavaExamplesCompiler(common.ExamplesCompiler):
    def __init__(self, path):
        common.ExamplesCompiler.__init__(self, 'java', '.java', path)

    def compile(self, src):
        args = ['/usr/bin/javac',
                '-cp',
                '/tmp/compiler/Tinkerforge.jar:.',
                '-Xlint',
                src]

        return subprocess.call(args) == 0

def run(path):
    return JavaExamplesCompiler(path).run()

if __name__ == "__main__":
    sys.exit(run(os.getcwd()))
