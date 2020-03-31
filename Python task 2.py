import random
import string
def get_details():
    first_name=input("Enter your First Name below \n")
    second_name=input("Enter your Second Name below \n")
    user_email=input("Enter your Email address below \n")
    return [first_name,second_name,user_email]

def get_password(f_name , l_name):
    letters= string.ascii_letters
    random_five= ''.join(random.choice(letters)for i in range(5))
    password= str(f_name[0:2] + l_name[-2:] + random_five)
    return password

def get_new_password(old_password):
    num=str(input('Do you want to enter a new password (yes or no) \n')).lower()
    if num== 'yes':
        new_password= input('Enter a new password of 7 characters or more \n')
        if len(new_password) >= 7:
            old_password = new_password
            return str(old_password)
        elif len(new_password)< 7:
            return get_new_password(old_password)
        else:
            return get_new_password(old_password)
    elif num == 'no':
        return str(old_password)
    elif num != 'yes' or num != 'no':
        return get_new_password(old_password)

def program():
    details=get_details()
    user_password=get_password(details[0],details[1])
    print ('your password is: ' +str(user_password))
    user_password=get_new_password(user_password)
    print ('your new password is: ' +str(user_password))
    details.append(str(user_password))
    return details

def main_program(d):
    d.append(program())
    decision = input("Do you want to input another user (yes or no): \n").lower()
    if decision == 'yes':
        return main_program(d)
    elif decision == 'no':
        return (d)

data=[]

data.append(main_program(data))
data.pop(-1)
labels=['First Name:','Last Name:','Email:','Password:']

print('*** HERE ARE THE DETAILS OF THE USERS ***')
for i in range(0, len(data)):
    print('User {0}'.format(i+1) + ' Details')
    for x in range(0,len(data[i])):
        print(labels[x]+' '+data[i][x])
