a = {}
def main():
    n = 0
    while True:
        try:
            a[n] = input("Name: ")
            n += 1
        except EOFError:
            break
    print()
    result()

def result():
    n = len(a)
    print("Adieu, adieu, to "+a[0], end="")
    if n > 2:
        for i in range(1,n-1):
            print (", "+a[i],end="")
        print(", and "+a[n-1])
    elif n == 2:
        print(" and "+a[n-1])
        
main()
