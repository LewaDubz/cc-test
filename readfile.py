my_file=open("testfile.txt","r")

for line in my_file:
    print(line.strip())

my_file.close

my_list=[]
my_list.append("Elso")
my_list.append("Masodik")
my_list.append("Harmadik")
my_file=open("testfile.txt","w")

for i in my_list:
    my_file.writelines(i)
my_file.writelines()
