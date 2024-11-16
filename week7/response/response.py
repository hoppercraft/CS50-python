import validators

def main():
    print(rep(input("What's your email address? ")))

def rep(m):
    ans = validators.email(m)
    if ans == True:
        return("Valid")
    else:
        return("Invalid")

main()
