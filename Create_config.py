import sys

with open("Config_change_request.txt") as f:
    lines = f.readlines()
with open("ONT_SFP_template.txt") as f:
    control_lines = f.readlines()

def remove_extra(list):
    new_list=[]
    
    for element in list:
        new_element=element.strip("\n")
        new_list.append(new_element)
    return new_list

lines=remove_extra(lines)
control_lines=remove_extra(control_lines)

###Check for Enable
if lines[0].strip("\n")!="Enable" or "enable":
    #sys.exit(-1)
    a=True
### check for config test line by line
#check for number of lines

if len(lines)!=len(control_lines):
    print("Configuation Error Number of lines does not match")
    sys.exit(-1)
#print(len(lines))
for step in range(len(lines)):
    if lines[step].find(control_lines[step])==-1:
        sys.exit(-1)