#!/usr/bin/env python3
import random
import argparse
import sys

class Diceware:
    def __init__(self, wordlist):
        self.wordlist_file = wordlist
        self.wordlist = {}
        self.import_wordlist()

    def import_wordlist(self):
        f = open(self.wordlist_file, 'r')
        for line in f.read().splitlines():
            if line.startswith('#'):
                continue
            if (len(line.split(' ', 1)) < 2):
                continue
            self.wordlist[line.split(' ', 1)[0]] = line.split(' ', 1)[1]
        f.close()

    def get_word_length(self):
        w = 'nope'
        while not w.isdigit():
            w = random.choice(list(self.wordlist.keys()))
        return len(w)
        
    def gen_word(self):
        r = ''
        for i in range(self.get_word_length()):
            r += str(random.randint(1, 6))
        try:
            return self.wordlist[r]
        except KeyError:
            print(f"Error: the wordlist does not contain the key {r}")
            print("There may be a missing number or lines with mixed lengths")
            sys.exit(1)

    def gen_passwd(self, leng=5):
        # leng = 5: number of words in pass
        passwd = ""
        for _ in range(leng):
            passwd += self.gen_word() + " "
        return passwd


def main(args):
    dw = Diceware(args.list)
    print(dw.gen_passwd(args.length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser("chillpass")
    parser.add_argument('-l', '--length', help="length of lookup number", type=int, default=5)
    parser.add_argument('-w', '--list', help="wordlist", type=str, default="diceware.wordlist")
    args = parser.parse_args()
    main(args)
    
