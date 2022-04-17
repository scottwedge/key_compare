#!/usr/bin/env python3

# Script to compare public key in local and remote files

# Functions

def extract_local_key(key_string):
    # Split string between spaces
    key = key_string.split()[1]  # Middle of three items is the local key
    return key


def extract_remote_key(key_string):
    # Split string between spaces
    key = key_string.split()[2]  # Take last/third item as the remote key
    return key

def min_len(key1, key2):  
    # Determine length of shortest key and use it as index when inspect elements in both keys
    return min(key1, key2)


def main():
    local_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCtYRg9XKmNmnxvsgV4ouR7JknFpyMrX//dvm9ardWE8qmuYkrGqNf5xcpEH+6dmuxJyEZKUsg+HmJLazQN5mdGCUhtGGw+UdEp0cfi3G+OXSmwupG0B1cZHf/TqRJ9OCiTrAOiGV+v083vyoWS7USQxcsCyMSNFto0p/o/7r0dIPng1hdnpTLArMbP8gnerIgvg+GSF4WNeXpT3KGfkfjUdFEY5Qr2Gvpo+F1F87EzkeUkAEfUklt1L707matRjEV30udDfTKvIOP+008nXwLCt/EwBQ9HUjYUcgSl6zw8ixd2V+uq8F3j8IPRQg8c8dY9G5H4BQ4CnABGAOC1hEPb3gAxDBG0lw6r9GV0nDswGqT3KyqsF4bxEWkoTyQCkiW6QKjk/Yra2HAO0QfP0knL2PmtscLq3wWYR/B1TxCL2UCuP9N0HfLpqCmtRXYag8sivppee+jSk/IIckRqEwjL9H/7BRG0ELC604JPIlXNB+ozq+6aCHX8jUD0weRHXt0= swedge@swedge-HP"
      
    remote_key1 = "|1|e2hrJ2SYhzWPsAuvOr50y5ezjAY=|U3dmQto/6EWDE55D5+Uas/BTTQM= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ=="
    
    remote_key2 = "|1|MbxcVaYxpIC6YMZ6XfyBsPpjlto=|uu6YwEYSKdjagL9lBOOeQ+ODxYE= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ=="
    
    remote_key3 = "|1|v8EnMAyuweayzeYu4MKdbAaZfow=|Ummwpz6Yk8dmhhE1RcWhR1JvdSQ= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ=="
    
    remote_key4 = "#|1|inekQd4CtExRu5bk+RkZSZ0EQ5g=|Hpf0N1yWrIqWLD87ZE81wi5jn8o= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCn35Dxd0zFzRmJNlHtCht15fNtZFCdIk73GKQlFIrDHsP5IlavukL+EYqJlmLUDTD6fJxmCHHbU88BnuaEmu/U="
    
    remote_key5 = "#|1|Dk99RzEhafXJYLGnjygpvuhBFPc=|rsE1EHNngg6FLMDrNiQ2IhpGeFg= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHFiVBv537BWEhTbrr3ZIou9REX2ngKLzk9t5WXFrDM7av3aub2GAuIay3JhbBEj+Lo8yqcrfrKt8BQfQVPUnAU="

    l_key = extract_local_key(local_key)
    print("Local key is:", l_key)
    
    for j in remote_key1, remote_key2, remote_key3, remote_key4, remote_key5:
        common_key = ""  # Init string
        r_key = extract_remote_key(remote_key1)
        print()  # Blank spacer line
        print("Remote key is:", r_key)
        
        min_l = min_len(l_key, r_key)
        
        for j in range(len(min_l)):
            if l_key[j] == r_key[j]:
                common_key = common_key + l_key[j]
            else:
                break
        
        print()  # Blank spacer line
        print("Common key to both local and remote keys is {} with length of {}.".format(common_key, len(common_key)))


if __name__ == "__main__":
    main()
