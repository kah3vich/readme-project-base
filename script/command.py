import json
import sys

from schema import schema_command


def main():

    rep_name = sys.argv[1:][0]

    print('✅ rep_name    ', rep_name)

    f = open('bd.json')
    
    data = json.load(f)
    
    for i in data['bd']:
        path = './cache/command.txt'
        title = i['title']

        if bool(rep_name) and title == rep_name:
            with open(path, 'w') as file:
                file.write(schema_command(i))
            return

        with open(path, 'w') as file:
            file.write(schema_command(i))

    f.close()

if __name__ == "__main__":
    main()