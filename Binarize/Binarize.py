my_file = open("textinput.txt") #opens file
whole_str = my_file.read() #reads file into a string
whole_length = len(whole_str) #takes length of string
whole_list = []
for i in range(0,whole_length):
    whole_list.append(whole_str[i]) #converts to list


databaseopen = open("database_1.txt") #reads in reference database
database_str = databaseopen.read()
data_base = {"\n":"011100", "-":"1011011"  
}
#print(database_str)
temp_data_base = database_str.split("\n") 
for i in range(0,len(temp_data_base)):
    index = temp_data_base[i].index("-")
    character = temp_data_base[i][0:index]
    end = len(temp_data_base[i])
    binarytemp = temp_data_base[i]
    binary = binarytemp[index +1:end] #converts database string to dictionary readable by function
    data_base.update({character:binary})

reverse_data_base = {"011100": "\n", "1011011":"-"
}

for i in data_base:
    reverse_data_base.update({data_base[i]:i}) #reverses database to be used if needed

#print(reverse_data_base)
fixes = {
}
#print(data_base)
for i in data_base:
    if (len(i) > 1) and (i != "/n"):
        fixes.update({i:data_base[i]}) #removes fixes and r
for i in fixes:
    data_base.pop(i)

#print(fixes)
reverse_fixes = {
}

for i in fixes:
    reverse_fixes.update({fixes[i]:i})
#print(reverse_fixes)

def binarize(tlist:list) -> str:
    result = ""
    i = 0 #counter
    while i < len(tlist):
        if i == len(tlist)-4: #stop mechaism to prevent index error
           result += data_base[tlist[i]]
           result += data_base[tlist[i+1]] #appends in remaining characters' corresponging binary code
           result += data_base[tlist[i+2]]
           result += data_base[tlist[i+3]]
           result2 = (str((len(result))) + "." + result)
           return result2
        elif tlist[i] + tlist[i+1] in fixes:
            result += fixes[tlist[i] + tlist[i+1]] # 2 long fixes
            i += 2 #adjusts counter
        elif tlist[i] + tlist[i+1] + tlist[i+2] in fixes: # 3 long fixes
            result += fixes[tlist[i] + tlist[i+1] +tlist[i+2]]
            i += 3 #adjusts counter
        elif tlist[i] + tlist[i+1] + tlist[i+2] + tlist[i+3] in fixes: # 4 long fixes
            result += fixes[tlist[i] + tlist[i+1] +tlist[i+2] + tlist[i+3]]
            i += 4 #adjusts counter
        elif tlist[i] + tlist[i+1] + tlist[i+2] + tlist[i+3] + tlist[i+4] in fixes: # 5 long fixes
            result += fixes[tlist[i] + tlist[i+1] +tlist[i+2] + tlist[i+3] + tlist[i+4]]
            i += 5 #adjusts counter
        elif tlist[i] + tlist[i+1] + tlist[i+2] not in fixes: #all other characters
            result += data_base[str(tlist[i])] #appends it onto result string
            i += 1 #adjusts counter

bi = open("binaryoutput.txt", "w")
bi.write(binarize(whole_list))
bi.close()
#print(binarize(whole_list))
#-------------------------------------------------------------------------------------------------
def binarize_number(int) -> str: #testing
    number_of_bits = 0
    parse_int = int
    while (parse_int) >= 2:
        parse_int /= 2
        number_of_bits += 1
    if number_of_bits == 0:
        return 1
    returned = []
    for i in range(number_of_bits):
        returned.append(0)
    saved_number = number_of_bits
    while number_of_bits != 0:
        if int / (2**number_of_bits) > 1:
            returned[saved_number-number_of_bits] = 1
        else:
            returned[saved_number-number_of_bits] = 1
        number_of_bits -= 1
    returned_str = ""
    for i in returned:
        returned_str += str(i)
    return returned_str

print(binarize_number(20))
print(binarize_number(1))
print(binarize_number(2))
print(binarize_number(3))