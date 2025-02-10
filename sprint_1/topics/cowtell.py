import cowsay
import sys

dir(cowsay)

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
