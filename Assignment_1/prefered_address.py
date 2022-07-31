from customer_details import *

def prefred_address(user):
    address = []
    data = []
    data1 =[]
    users_list = [ key for key in cust_accounts.keys() ]
    if user in users_list:
        pref_add_type = cust_accounts.get(user).get('Address',{}).get('Preferred')
        pref_add = cust_accounts.get(user).get('Address').get(pref_add_type)
        if not pref_add_type:
            pass
        else:
            for values in cust_accounts.get(user).get('Address',{}).get(pref_add_type,{}).values():
                address.append(values)
            data = [{user: address}]
        return data
    elif user == 'all':
        for usr in users_list:
            pref_add_type = cust_accounts.get(usr).get('Address',{}).get('Preferred',{})
            if not pref_add_type:
                pass
            else:
                for values in cust_accounts.get(usr).get('Address',{}).get(pref_add_type,{}).values():
                    address.append(values)
                data = [{usr: address}]
            data1.append(data)
        return data1
            
            
        

if __name__ == "__main__":
    name = input('Enter the customer Name or 'all' to get data for everyone\n')
    pref_address = prefred_address(name)
    print(f"Prefred address {pref_address}") 