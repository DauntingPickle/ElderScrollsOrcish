x = 1
list = []

def orc2eng():
    count = 0
    orcword=str(input("Enter the Orcish word you would like to translate: "))
    if orcword == "exit":
        exit()
    with open("orcishwords.txt", 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if orcword in line:
            list.insert(count, line)
            count += 1
        
    if len(list) > 0:
        lineLen = len(list)
        print(list[0])
        #for i in range(lineLen):
            #print(end=list[i])
        print(list)

       
def eng2orc():
    count = 0
    engword=str(input("Enter the english word you wish to translate: "))
    if engword == "exit":
        exit()
    with open("orcishwords.txt", 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if engword in line:
            list.insert(count, line)
            count += 1
        
    if len(list) > 0:
        lineLen = len(list)
        print(list[0])
        #for i in range(lineLen):
            #print(end=list[i])

while x == 1:
    ask=(str(input("Enter either orc or eng to choose which language to translate from: ")))
    if ask == "orc":
        orc2eng()
    elif ask == "eng":
        eng2orc()
    elif ask == "exit":
        exit()
    else:
        print("Invalid input")


