with open("/usr/share/dict/words") as f:
    line_one = f.readline()
    print(line_one)


def testPrint(word):
    print(word)


testPrint("Hello world")
