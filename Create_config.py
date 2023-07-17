with open("Config_entry.txt") as f:
    lines = f.readlines()
with open("Config_change_request.txt") as f:
    template = f.readlines()

number_of_command=0
line_no=0
while number_of_command>15:

    if template[number_of_command]==" \n":
        template[number_of_command]=lines[line_no]
        line_no+=1
    number_of_command+=1
#print(template)

with open('Config_change_request.txt', 'w') as f:
    for line in template:
        f.write(line)
        
