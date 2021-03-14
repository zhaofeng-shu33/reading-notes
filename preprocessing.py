# preprocessing before typesetting
import argparse
def split_md(filename):
    f = open(filename)
    title = f.readline().lstrip('#').lstrip(' ').rstrip('\n')
    content = f.read().lstrip('\n')
    return title, content

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename')
    args = parser.parse_args()
    title, content = split_md(args.filename)
    template = open('template.tex').read()
    template = template.replace('#title', title)
    template = template.replace('#text', content)
    output_name = args.filename.split('/')[-1].replace('.md', '.tex')
    with open('build/' + output_name, 'w') as f:
        f.write(template)
 
