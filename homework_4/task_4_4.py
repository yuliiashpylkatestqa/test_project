from task_3 import alphabet

def CreateList(input_list):
    output_list = [alphabet(item) for item in input_list if type(item)== str]
    return output_list
if __name__=="__main__":
    l = ["sfd34",456,'sfd']
    print(CreateList(l))
