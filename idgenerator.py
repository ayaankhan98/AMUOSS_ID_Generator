from getpass import getpass
from hashlib import sha256
from texttable import Texttable

Logo = '''
        
           __  __ _    _         ____   _____ _____ 
     /\   |  \/  | |  | |       / __ \ / ____/ ____|
   /  \  | \  / | |  | |______| |  | | (___| (___  
  / /\ \ | |\/| | |  | |______| |  | |\___ \\___ \ 
  / ____ \| |  | | |__| |      | |__| |____) ____) |
 /_/    \_|_|  |_|\____/        \____/|_____|_____/ 
                                                    
  '''

def authenticate(password):
    hashed_pass = sha256(password.encode('utf-8')).hexdigest()

    with open('hashedpass.txt','r') as f:
        correct_pass = f.readline()

    if hashed_pass == correct_pass:
        print('Login successful')
        return True
    return False

def validate_name(name):
    for part in name.split():
        if part.isalpha():
            return True
        return False

def take_name_input(prompt):
    name = input(prompt)
    while not validate_name(name):
        print("You did not enter the correct name Please Try Again!")
        name = input(prompt)
    return name

def get_user_info():
    user_info = []
    user_info.append(take_name_input("Enter Your Name : "))
    user_info.append(input("Enter Slack username : "))
    user_info.append(take_name_input("Enter Mother Name : "))
    user_info.append(take_name_input("Enter Father Name : "))
    return user_info

def print_id(user_info):
    table = Texttable()
    table.add_rows([[f"{Logo}\nMember - {user_info[0]}"],
                    [f"slack username - {user_info[1]}"],
                   [f"Mother Name - {user_info[2]}"],
                   [f"Father Name - {user_info[3]}"]
                   ])
    print(table.draw())

def main():
    password = getpass("Enter Admin Password : ")
    if authenticate(password):
        print_id(get_user_info())

if __name__ == "__main__":
    main()