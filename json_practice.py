import json

dict1 = {"name" : "song", "age" : 10}

print("dict1 : %s" % dict1)
print("dict1 type : %s" % type(dict1))

print("name : %s" %dict1.get("name"))
print("============")

#convert dictionary to json using json.dump
json_val = json.dumps(dict1, indent=2)

print("json_val : %s" %json_val)
print("json_val type : %s" % type(json_val))

print("==============")

dict2 = json.loads(json_val)
print("dict2 : %s" % dict2)
print("dict2 type : %s" % type(dict2))



######### list

temp = list([2,3,4,5])
temp_new = list()

for i in temp:
    temp_new.append(i*2)

print(temp_new)

temp_new2 = list([i*2 for i in temp_new])
print(temp_new2)
temp_new3 = list([i**2 for i in temp_new2])
print(temp_new3)