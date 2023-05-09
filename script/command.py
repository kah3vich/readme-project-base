import json

from schema import schema_command


def main():
    f = open('bd.json')
    
    data = json.load(f)
    
    for i in data['bd']:
        path = './cache/command.txt'

        with open(path, 'w') as file:
            file.write(schema_command(i))

    f.close()

if __name__ == "__main__":
    main()