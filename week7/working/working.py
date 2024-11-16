import re

def main():
    time = convert(input("Hours: "))
    print(time)

def convert(s):
    s=s.strip()
    if matches := re.search(r"^(\d|1[0-2])\:?([0-5]\d)? ([AP]M) to (\d|1[0-2])\:?([0-5]\d)? ([AP]M)$",s):
        t1 = int(matches.group(1))
        try:
            t2 = int(matches.group(2))
        except TypeError:
            t2 = 0
        t3 = int(matches.group(4))
        try:
            t4 = int(matches.group(5))
        except TypeError:
            t4 = 0
        x = matches.group(3)
        y = matches.group(6)
        if x == "PM":
            t1 = t1+12
        elif t1==12:
            t1 = t1-12
        if y == "PM" and t3 == 12:
            t3 = t3
        elif y=="PM":
            t3 = t3+12
        return(f"{t1:02}:{t2:02} to {t3:02}:{t4:02}")
    else:
        raise ValueError


if __name__ == "__main__":
    main()
