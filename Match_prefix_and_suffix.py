def mix(name1 : list,name2 : list):
    counter = -1

    while counter != len(name1) or counter != len(name2):
        for i in range (0,(len(name1))):
            counter += 1
            if name1[(-1)-counter] == name2[0+counter]:
                del name2[0+counter]
                continue
            elif name1[(-1)-counter] != name2[0+counter]:
                break
        
        result = name1 + name2
        return result


name1 = list(input("enter first word -> "))
name2 = list(input("enter a second word -> "))

print(mix(name1,name2))











