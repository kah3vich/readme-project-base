python main.py - create readme file for projects

python command.py - create bash script

cat ./cache/command.txt | bash - active bash command

## Script:

### Base:

```bash
cd script/; python main.py; python command.py; cat ./cache/command.txt | bash; rm -rf cache/reps/*; cd ..;
```

### Custom project [name]:

```bash
cd script/; python main.py; python command.py [name]; cat ./cache/command.txt | bash; rm -rf cache/reps/*; cd ..;
```

### Clear cache:

```bash
rm -rf script/cache/readme/*; rm -rf script/cache/reps/*;
```
