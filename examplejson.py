import json

# lets start with a python structure and convert it to json string
python_object = {'some_text': 'my text',
                 'some_number': 12345,
                 'null_value': None,
             'some_list': [1,2,3]}

# here we are converting python object to json string
json_string = json.dumps(python_object)

# json_string = '{"some_list": [1, 2, 3], "some_text": "my text",
#                 "some_number": 12345, "null_value": null}'
# api converts a python dictionary to json object and vice versa
# At this point we have a json_string in our hands. Now lets convert it back to pyton structure
new_python_object = json.loads(json_string)

# new_python_object = {u'some_list': [1, 2, 3], u'some_text': u'my text',
#                      u'some_number': 12345, u'null_value': None}