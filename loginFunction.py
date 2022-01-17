import json

def login(user_name,Email,pasword):

    with open('Index.json', 'r') as f:
        ac = json.load(f)
        if (user_name in ac and ac[user_name][0] == Email) :
            if ac[user_name][1] == pasword:
                return "login succesfull Hi", user_name
            else:
                return"incorect user name or pasword please try again"
        else:
            option = input('Incorect user name or pasword or you need to signup first for signup entere "y" or for login please tyr again : ')
            if option == "y":
                signup()
            else:
                return exit()


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


