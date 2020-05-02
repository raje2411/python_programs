#Input of Dictionaries
user1 = {'admin': True, 'active': True, 'name': 'Kevin'}
user2 = {'admin': False, 'active': True, 'name': 'Rajesh'}
user3 = {'admin': False, 'active': False, 'name': 'Dinesh'}
user4 = {'admin': True, 'active': False, 'name': 'Amar'}
user5 = {'admin': True, 'active': True, 'name': 'Kevin1'}
user6 = {'admin': False, 'active': True, 'name': 'Rajesh1'}
user7 = {'admin': False, 'active': False, 'name': 'Dinesh1'}
user8 = {'admin': True, 'active': False, 'name': 'Amar1'}
user9 = {'admin': True, 'active': True, 'name': 'Kevin2'}
user10 = {'admin': False, 'active': True, 'name': 'Rajesh2'}
user11 = {'admin': False, 'active': False, 'name': 'Dinesh2'}
user12 = {'admin': True, 'active': False, 'name': 'Amar2'}

users_dict_list = [user1,user2,user3,user4,user5,user6,user7,user8,user9,user10,user11,user12]

# print(type(users_dict_list))
line = 1;
for user in users_dict_list :
    if user['active'] and user['admin']:
        print(f"{line} User: {user['name']} is ACTIVE - (ADMIN)")
    elif user['active']:
        print(f"{line} User: {user['name']} is ACTIVE")
    elif user['admin']:
        print(f"{line} User: {user['name']} is (ADMIN)")
    else:
        print(f"{line} User: {user['name']} is Neither Active nor Admin")
    line += 1
