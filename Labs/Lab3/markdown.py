"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

blockquote = False
bq = ''
for line in fileinput.input():
  line = line.rstrip() 
  line = convertStrong(line)
  line = convertEm(line)
  if line[0] == '>' and blockquote == False:
    blockquote = True
    bq = '\t'
    line = line[2:]
    print '<blockquote>'
  elif line[0] == '>':
    line = line[2:]
  elif line[0] != '>' and blockquote == True:
    blockquote = False
    bq = ''
    print '</blockquote>'
  if line[0] == '#':
    if line[1] == '#':
      if line[2] == '#':
        print bq+'<h3>' + line[4:] + '</h3>',
      else:
        print bq+'<h2>' + line[3:] + '</h2>',
    else:
      print bq+'<h1>' + line[2:] + '</h1>',
  else:
    print bq+'<p>' + line + '</p>',
