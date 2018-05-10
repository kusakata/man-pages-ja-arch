import sys
import json
import re
import subprocess

with open(sys.argv[1], 'r') as f:
    info = json.load(f)
    file = './output/html/man/' + sys.argv[1][4:-5] + '.html'
    with open(file, 'r') as g:
        org = g.read()
    with open(file, 'w') as g:
        new = '<a href="https://www.archlinux.jp/packages/?name=' + info['package'] + '">' + info['package'] + '</a><sup>' + info['version'] + '</sup>'
        g.write(re.compile('<a.+> View page source<\/a>').sub(new, org))
