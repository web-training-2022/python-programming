from customer_details import *

def prefred_address(user):
    address = []
    data = []
    data1 = []
    users_list = [ key for key in cust_accounts.keys() ]
    if user in users_list:
        pref_add_type = cust_accounts.get(user).get('Address',{}).get('Preferred')
        if not pref_add_type:
            data = "No Address is Mentioned"
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
    name = input('Enter all to see everyone address or specific to see perticular\n')
    if name == 'all':
        pref_address = prefred_address(name)
        print(f"Prefred address: {pref_address}") 
    elif name == 'specific':
        name = input('Enter the name of the person\n')
        pref_address = prefred_address(name)
        print(f"Prefred address: {pref_address}") 
    else:
        print("Something Wrong")
    
    