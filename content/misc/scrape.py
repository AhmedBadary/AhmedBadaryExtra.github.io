import os
from functools import reduce
import re


def all_files(directory):
    for path, dirs, files in os.walk(directory):
        for f in files:
            yield os.path.join(path, f)

md_files = [f for f in all_files('research')
               if f.endswith('.md')]

# print(md_files)



# new_lines = []
# for f_name in md_files:
#     with open(f_name, 'r') as f:
#         lines = f.read().split('\n')
#     new_lines.append(get_page_title(lines))

def get_page_title(lines):
    for l in lines:
        if "title: " in l:
            return l[len("title: "):]
    print('failed to find title')
    return 'NO-TITLE'




def get_titles(lines):
    titles = []
    for l in lines:
        if "# " in l[:2] and l not in incomplete and l not in history:
            titles.append(l)
    return titles

def splitkeepsep(s, sep):
    return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if elem == sep else acc + [elem], re.split("(%s)" % re.escape(sep), s), [])

def get_everything(md_files):
    new_lines = []
    for f_name in md_files:
        with open(f_name, 'r') as f:
            # lines = f.read().split('\n')
            lines = f.read()
        lines = splitkeepsep(lines, '\n')
        # new_lines.append(get_page_title(lines) + '\n\n')
        k = 0
        for i, l in enumerate(lines):
            if "***" == l.strip() and "***" == lines[i+1].strip():
                k = i + 2
                break
        if k == 0:
            print(f_name)
            continue
        new_lines.append('TITLE: ' + get_page_title(lines))
        new_lines.append('LINK: ' + f_name + '\n\n')
        for l in lines[k:]:
            if ("Asynch" in l and not "-->" in l and not "<!--" in l) or not l:
                continue
            new_lines.append(l)
        new_lines.append('\n\n***\n***\n\n')
    return new_lines

all_lines = get_everything(md_files)
with open('everything.md', 'w') as f:
    for l in all_lines:
        # if '    ' not in l[:5]:
        #     f.write('\n' + l + '\n')
        # else:
        #     f.write(l + '\n')
        f.write(l)