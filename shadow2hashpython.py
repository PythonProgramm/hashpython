false = ["*", "!", "x"]
from sys import argv


def getShadow(file):
    pwd = ""

    with open(file) as file:
        for i in file.readlines():
            i = i.rstrip("\n")
            i = i.split(":")[1]
            if not i in false:
                pwd = i
    return pwd


if len(argv) != 2:
    print("USAGE:\n[SHADOWFILE]")
    exit(1)

if __name__ == '__main__':
    result = getShadow(argv[1])

    if result == "":
        print("No hash found in shadow file")
        exit(1)
    else:
        print(result)
