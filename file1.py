#
# This is a global module:

# checkKey is a function that performs a key check in a dictionary:
# It returns 3 output elements (dict key pair, string msg, and literal (Yes/No).
# It returns 2 output elements (string msg, and literal (Yes/No).

def checkKey(dict_key, dictionary):
    
    if dict_key in dictionary:
       
        """ Extract the value paired with the found key """ 
        value = dictionary.get(dict_key)
        print()
        print(dict_key, " : ", dictionary[dict_key], "record is found in dictionary!")
        found="Yes"
        return found
    else:
        print(" key is not found in dictionary!")
        found="no"
        return found
#