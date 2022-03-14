"""
write a function to flatten a nested dictionary. Namespace the keys with a period.

ex: 

input:

{
    "key" : 3, 
    "foo" : {
        "a" : 5,
        "bar" : { "baz" : 8}
    }
}


output: 

{
    "key" : 3,
    "foo.a": 5,
    "foo.bar.baz" : 8
}

"""

def flatter_json_array(data):

    output = {} # To store output

    # Loop through the json 
    for k, v in data.items():

        if isinstance(v, dict): # if value contain key value pair 

            flat_sub_dict = flatter_json_array(v) 

            for fk, fv in flat_sub_dict.items(): # loop through the nested json

                output[f'{k}.{fk}'] = fv # push value into output dict
        else:
            output[k] = v

    return output


input_x = {
    "key" : 3, 
    "foo" : {
        "a" : 5,
        "bar" : { "baz" : 8}
    }
}


print(flatter_json_array(input_x))
