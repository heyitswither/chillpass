# chillpass

Just a simple diceware script written in Python

```
usage: chillpass [-h] [-l LENGTH] [-w LIST]

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH    length of lookup number
  -w LIST, --list LIST    alternate wordlist
```

Type `make deps` to download and verify the official diceware wordlist. You can also use your own wordlist. A wordlist is a list of words, each on their own line, starting with a number. See the following example.

```
1 it's
2 the
3 end
4 of
5 the
6 world
```

The numbers have to all be the same length. Lines that contain more than just numbers 1-6 will be ignored. Comment are lines that start with a '\#'. Lookup numbers do not need to be in order, but it is preferred for them to be. The following wordlist will not cause any errors.

```
what this
2 hello boy
6 well
# jeck
1 hmm
4 idk
3 fair enough
5 whatever
```
