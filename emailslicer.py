def emailslicer():
    print("welcome to email slicer")
    print("")

    email_input=input("enter your email address: ")
    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")

    print("username:    ",username)
    print("domain:   ",domain)
    print("extension:   ",extension)

emailslicer()