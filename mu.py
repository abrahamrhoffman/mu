
class Rules(object):

    def __init__(self):
        pass

    def one(self, aString):
        if ("I") == aString[-1]:
            aString = aString + ("U")
        return aString

    def two(self, aString):
        aString = aString[0] + (aString[1:]*2)
        return aString

    def three(self, aString):
        if ("III") in aString:
            aString = aString.replace("III", "U")
        return aString

    def four(self, aString):
        if ("UU") in aString:
            aString = aString.replace("UU", "")
        return aString


def main():
    rules = Rules()
    aString = ("MI");print(aString)
    # The following rules demonstrate that the system is unsolvable
    aString = rules.two(aString);print(aString)
    aString = rules.two(aString);print(aString)
    aString = rules.two(aString);print(aString)
    aString = rules.three(aString);print(aString)
    aString = rules.four(aString);print(aString)

if __name__ == "__main__":
    main()
