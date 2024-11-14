#!/usr/bin/env python3
# Converts an exported Storybook Weaver Web Document to work on github pages
import os, sys
import glob
import fileinput

# First, change title.htm to index.html
try:
    os.rename('title.htm', 'index.html')
except FileNotFoundError:
    print("title.htm not found")
# Now we need to change the reference in any files to the index document
for fn in glob.glob('*.htm'):
    print(fn)
    with open(fn, 'r+b') as f:
        contents = f.read()
        if b'title.htm' in contents:
            contents = contents.replace(b'title.htm', b'index.html')
            f.seek(0)
            f.write(contents)
