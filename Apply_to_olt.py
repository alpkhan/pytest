print("Deploy")


with open("Config_change_request.txt") as f:
    lines = f.readlines()

with open('OLT_config.txt', 'a') as f:
    for line in lines:
        f.write(line)
        f.write('\n')







before_list=["enable","config"," ","tcont 4 dba-profile-id 20","gem add 12 eth tcont 4 cascade on","gem mapping 12 1 vlan 300","commit","quit"," ","ont-port eth adaptive pots adaptive","commit","quit","interface gpon 0/3","ont port native-vlan 1 1 eth 1 vlan 300"]


with open('Config_change_request.txt', 'w') as f:
    for line in before_list:
        f.write(line)
        f.write("\n")
