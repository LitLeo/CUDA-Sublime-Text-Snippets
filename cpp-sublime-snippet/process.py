import os
import string
import re

for f in os.listdir('.'):
    print f
    if f.find('snippet') != -1: