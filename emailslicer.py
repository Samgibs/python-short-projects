def main():
    print("welcome to the email slicer!")
    print("")

    email_input=input("input your emailaddress: ")
    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")

    print("username :   ",username)
    print("domain:  ",domain)
    print("extension:   ",extension)


main()