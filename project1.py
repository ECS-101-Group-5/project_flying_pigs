my_file = open("textinput.txt") #opens file
whole_str = my_file.read() #reads file into a string
whole_length = len(whole_str) #takes length of string
whole_list = []
for i in range(0,whole_length):
    whole_list.append(whole_str[i]) #converts to list

databaseopen = open("database_1.txt")
database_str = databaseopen.read()
data_base = {"\n":"011011"
}

temp_data_base = database_str.split("\n")
for i in range(0,len(temp_data_base)):
    index = temp_data_base[i].index("-")
    character = temp_data_base[i][0:index]
    end = len(temp_data_base[i])
    binarytemp = temp_data_base[i]
    binary = binarytemp[index +1:end]
    data_base.update({character:binary})

reverse_data_base = {"011011": "\n"
}

for i in data_base:
    reverse_data_base.update({data_base[i]:i})

#print(reverse_data_base)
fixes = {
}
print(data_base)
for i in data_base:
    if (len(i) > 1) and (i != "/n"):
        fixes.update({i:data_base[i]})
for i in fixes:
    data_base.pop(i)

print(fixes)
reverse_fixes = {
}

for i in fixes:
    reverse_fixes.update({i:fixes[i]})

def binarize(tlist:list) -> str:
    result = ""
    for i in range(len(tlist)):
        for n in fixes:
            if i == len(tlist)-2:
               result += data_base[tlist[i]]
               return result
            elif tlist[i] + tlist[i+1] + tlist[i+2] == n:
                result += fixes[tlist[i] + tlist[i+1] +tlist[i+2]]
            else:
                result += data_base[tlist[i]] #appends it onto result string
    
#print(whole_str)
#print(whole_list)
#print(binarize(whole_list))

def debinarize(tstring:str) -> str:
    result = ""
    index = 0
    while index < len(tstring):
        if tstring[index] == "1":
            if tstring[index+1] == "1":
                result += reverse_fixes[tstring[index:index +7]]
            else:
                result += reverse_data_base[tstring[index:index+7]]
            index += 7
        if tstring[index] == "0":
            result += reverse_data_base[tstring[index:index+6]]
            index += 6
    return result 
print(debinarize(binarize(whole_list)))

if (debinarize(binarize(whole_list))) == whole_str:
    print(True)
else:
    print(False)