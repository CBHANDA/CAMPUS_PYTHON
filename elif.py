s1=set()
while True:
    print("***ENTER EMAIL***")
    print("1. Add")
    print("2. Search")
    print("3. remove")
    print("4. list")
    print("5. exit")
    opt=int(input("enter your option"))
    if opt==1:
        email_id=input("enter eamil-id")
        if email_id in s1:
            print("thyis email exists")
        else:
            s1.add(email_id)
    elif opt==2:
        email_id=input("enter email id ")
        if email_is in s1:
            print("email id is found")
    elif opt==3:
        email_id=input("enter email id ")
        if email_id in s1:
            email_set.remove(email_id)
        else:
            print("this email id not exists")
    elif opt==4:
        for email_id in s1:
            print(email_id)
    elif opt==5:
        break