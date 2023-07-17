import sys


with open("Config_change_request.txt") as f:
    lines = f.readlines()
with open("ONT_SFP_template.txt") as f:
    control_lines = f.readlines()

###Check for Enable
if lines[0].strip("\n")!="Enable" or "enable":
    #sys.exit(-1)
    a=True
###Check for config mode
if lines[1].strip("\n")!="Config" or "config":
    #sys.exit(-1)
    b=True
###Check for Line profile
lineprofile=lines[2].strip("\n")
lineprofile=lineprofile.split(control_lines[2].strip("\n"))
profile_id=lineprofile[1].strip(" ")

if profile_id.isnumeric()==False:
    
    sys.exit(-1)    
###Check for servis profile
service=lines[8].strip("\n")
service=service.split(control_lines[8].strip("\n"))
service_id=service[1].strip(" ")

if service_id.isnumeric()==False:
    
    sys.exit(-1) 