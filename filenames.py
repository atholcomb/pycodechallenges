#!/usr/bin/python3.7
# written by: atholcomb
# filenames.py

import os
from pathlib import Path

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new = { fn : fn for fn in filenames }
new = [(z, Path(z).stem + '.h') if '.hpp' in z else (z, z) for z in new]
print(new)

#print(newfilenames) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
