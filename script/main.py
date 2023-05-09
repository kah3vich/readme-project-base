import glob
import json
import os
import shutil

from schema import schema_readme


def remove_cache():
    folder = './cache/readme'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def main():

    remove_cache()

    f = open('bd.json')
    
    data = json.load(f)
    
    for i in data['bd']:
        title = i['title']
        path = f'./cache/readme/{title}.md'
        with open(path, 'w') as file:
            file.write(schema_readme(i['url'], i['title'], i['subtitle'], i['description'], i['links'], i['stacks'], i['developers']))

    f.close()

if __name__ == "__main__":
    main()