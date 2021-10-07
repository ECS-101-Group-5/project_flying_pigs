my_file = open("textinput.txt") #opens file
whole_str = my_file.read() #reads file into a string
whole_length = len(whole_str) #takes length of string
whole_list = []
for i in range(0,whole_length):
    whole_list.append(whole_str[i]) #converts to list

databaseopen = open("database_1.txt")
database_str = databaseopen.read()
data_base = {"\n":"11101"
}

temp_data_base = database_str.split("|\n")
for i in range(0,len(temp_data_base)):
    index = temp_data_base[i].index("-")
    character = temp_data_base[i][0:index]
    end = len(temp_data_base[i])
    binarytemp = temp_data_base[i]
    binary = binarytemp[index +1:end]
    data_base.update({character:binary})

reverse_data_base = {"11101": "\n"
}

for i in data_base:
    reverse_data_base.update({data_base[i]:i})

print(reverse_data_base)

def binarize(tlist:list) -> str:
    result = ""
    if data_base[tlist[0]] == 6:
        result += 1
    if data_base[tlist[0]] == 5:
        result += 0
    for i in tlist:
        result += data_base[i] #appends it onto result string
    return result
#print(whole_str)
#print(whole_list)
print(len(binarize(whole_list)))

def debinarize(tstring:str) -> str:
    result = ""
    index = 0
    while index < len(tstring):
        if tstring[index] == 1:
            result += reverse_data_base[tstring[index:index+6]]
            index += 6
            print(index)
        if tstring[index] == 0:
            result += reverse_data_base[tstring[index:index+5]]
            index += 5
            print(index)
    return result 

print(debinarize(binarize(whole_list)))