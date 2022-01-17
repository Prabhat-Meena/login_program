import json

def signup():
    user_name = input("Enter your name: ")
    Email = input("Enter your Email-id: ")
    pasword = input("Enter your pasword: ")
    with open('index.json', 'r') as f:
        ac = json.load(f)

        ac[user_name] = [Email,pasword]

        ac = json.dumps(ac, indent=4)

        with open('Index.json', 'w') as f:
            f.write(ac)
            print('Signup complete \nWelcom',user_name)

def login():
    user_name = input("Enter your name: ")
    Email = input("Enter your Email-id: ")
    pasword = input("Enter your pasword: ")

    with open('Index.json', 'r') as f:
        ac = json.load(f)
        if (user_name in ac and ac[user_name][0] == Email) :
            if ac[user_name][1] == pasword:
                print("login succesfull \nHi", user_name)
            else:
                print("incorect user name or pasword please try again")
                login()
        else:
            print('Incorect user name or pasword or you need to signup first')
            option = input('Do you want to signup or login first for signup entere "y" or for login enter "n" : ')
            if option == "y":
                signup()
            elif option == "n":
                login()
            else:
                print('you must enter "y" or "n"')