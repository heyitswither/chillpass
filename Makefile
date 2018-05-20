WGET=wget

deps:
	$(WGET) http://world.std.com/~reinhold/diceware.wordlist.asc
	@gpg diceware.wordlist.asc || $(RM) diceware.wordlist.asc

clean-deps:
	$(RM) diceware.wordlist
