def print_lol(the_list,indent=False,level=0):  # Addition of the DEFUALT value for level has made it optional
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            if indent:
                for tabs in range(level):
                    print("\t", end="")
            print(each_item)


