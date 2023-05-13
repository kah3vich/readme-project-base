import json
import sys

from schema import schema_command


def main():

    rep_name = sys.argv[1:][0]

    f = open('bd.json')
    
    data = json.load(f)

    result = 'cd ./cache/reps/; rm -rf ./* \n\n'
    
    for i in data['bd']:
        path = './cache/command.txt'
        title = i['title']

        if bool(rep_name) and title == rep_name:
            with open(path, 'w') as file:
                file.write('cd ./cache/reps/; rm -rf ./* \n\n' + schema_command(i) + 'cd ../..;')
            return

        result += schema_command(i)

    result += 'cd ../..;'

    with open(path, 'w') as file:
        file.write(result)

    f.close()

if __name__ == "__main__":
    main()