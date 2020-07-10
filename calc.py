import pdb, sys

def add(x, y):
    print(float(x) + float(y))

def sub(x, y):
    print(float(x) - float(y))

def mul(x, y):
    print(float(x) * float(y))

def div(x, y):
    print(float(x) / float(y))

def main(argv):
    if (argv[0] == 'add'):
        add(argv[1],argv[2])
    elif (argv[0] == 'sub'):
        sub(argv[1],argv[2])
    elif (argv[0] == 'div'):
        div(argv[1],argv[2])
    elif (argv[0] == 'mul'):
        mul(argv[1],argv[2])
    else:
        print("Use add/sub/div/mul to do a calculation. I'm not that advanced.")


if __name__ == "__main__":
    main(sys.argv[1:])
