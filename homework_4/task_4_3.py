def OnlyNumberFromList(list1):
    l = [item for item in list1 if type(item)==int or type(item)==float]
    return l
if __name__=="__main__":
    start_list=[445, 664.3, "df", "44", 67.3, 0, [78,90]]
    finish_list = OnlyNumberFromList(start_list)
    print(finish_list)