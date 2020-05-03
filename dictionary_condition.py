#!/usr/bin/env python3.7

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


'''
Output will look like this:-

1 User: Kevin is ACTIVE - (ADMIN)
2 User: Rajesh is ACTIVE
3 User: Dinesh is Neither Active nor Admin
4 User: Amar is (ADMIN)
5 User: Kevin1 is ACTIVE - (ADMIN)
6 User: Rajesh1 is ACTIVE
7 User: Dinesh1 is Neither Active nor Admin
8 User: Amar1 is (ADMIN)
9 User: Kevin2 is ACTIVE - (ADMIN)
10 User: Rajesh2 is ACTIVE
11 User: Dinesh2 is Neither Active nor Admin
12 User: Amar2 is (ADMIN)
'''
