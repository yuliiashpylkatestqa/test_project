def alphabet(line_str):
    s=''
    for item in line_str:
        if item.isalpha():
            s=s+item
    assert s.isalpha()
    return s

if __name__=="__main__":
    l=alphabet("w567hjjj@@4hjkh")
    print(l)
# jj=["jffjk,,f", 67]
# jj.remove(67)
# print(jj)