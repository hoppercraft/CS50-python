import re

def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"\bum\b",s , flags = re.IGNORECASE)
    return(len(um))

if __name__ == "__main__":
    main()
