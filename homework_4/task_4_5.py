from task_3 import alphabet

def DictGen1(dict1):
    dict_out = {k:type(dict1[k]) for k in dict1}
    return dict_out

def DictGen2(dict1):
    dict_out = {k:alphabet(dict1[k].lower()) for k in dict1 if type(dict1[k])==str}
    return dict_out

if __name__=="__main__":
    dict = {"name":"Iuliia", "surname":"Shpylka", "age":29, "position":"QA", "address":"Komarova 46", "skills":"Cook"}
    d = DictGen1(dict)
    print(d)
    d = DictGen2(dict)
    print(d)
    z = [];
    z.append("ds")
    print(z)
    z.append(["ds","ds"])
    print(z)

