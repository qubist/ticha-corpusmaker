import os
import re
import sys

# cleans a directory of Ticha Handwritten Text downloads, outputs into a new,
# parallel directory
def cleanDir(dirname):
    os.makedirs("clean-output", exist_ok=True)

    for filename in [filename for filename in os.listdir(dirname) if filename.endswith('.txt')]:
        with open(f'clean-output/{filename.split(".")[0]}-clean.txt', 'w') as f:
            f.write(cleanFile(os.path.join(dirname, filename)))

# Takes a filename and returns the contents of the file, cleaned
def cleanFile(filename):
    print(f'Cleaning {filename.split("/")[-1]}')
    with open(filename, 'r') as f:
        fileContent = f.read()

    out = removeHTML(fileContent)
    out = fixWhitespace(out)
    # out = removeMeta(out)
    return out

# removes HTML from text, returns new text
def removeHTML(text):
    out = re.sub('<!--.*?-->', '', text) # remove HTML comments
    out = re.sub('(<.*?>)|(<.*?/>)', '', out) # remove HTML tags
    return out


# fixes annoying whitespace issues
def fixWhitespace(text):
    text = re.sub(r'^\s*', '', text, flags=re.MULTILINE) # remove leading whitespace
    text = re.sub(r'\s*$', '', text, flags=re.MULTILINE) # remove trailing whitespace
    return text

# removes page and line numbers
def removeMeta(text):
    text = re.sub('\[[0-9]*?(r|v)?\]', '', text) # remove bracketed page numbers
    text = re.sub('\([0-9]*?(r|v)?\)', '', text) # remove parenthesized page numbers
    text = re.sub('^[0-9]*?', '', text) # remove start-of-line numbers
    text = re.sub('(\[.*?\])', '\\1', text) # remove other brackets from text
    text = re.sub('(\(.*?\))', '\\1', text) # remove parentheses from text
    text = re.sub('\?', '', text) # remove question marks from text
    return text

cleanDir(sys.argv[1])
