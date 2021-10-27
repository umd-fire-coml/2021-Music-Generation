# How do I use this? Just call check_env() to see if you have the correct
# packages installed. If it returns false, it will print out what packages
# are required. If it returns true, no further action required.
#
# Do you need to add another package? This just checks the environment.yml
# for valid packages, so this checker won't break.

import os

def check_env():

    ccfile = open("environment.yml", "r")
    atPackages = False
    isHere = False
    isInstalled = True
    env_packages = []
    installed_packages = []

    for aline in ccfile:
        values = aline.split()
        if(atPackages == True):
            env_packages.append(values[1])
        if(values[0] == "dependencies:"):
            atPackages = True
    ccfile.close()

    out = []
    out = os.popen('conda env export').read().split()

    for name in env_packages:
        if "=" in name:
            terminator = name.index('=')
            name = name[:terminator]
        for line in out:
            if name in line:
                isHere = True
                break
        if isHere is False:
            print(f"{name} is not installed!")
            isInstalled = False
        isHere = False
    
    if isInstalled is True:
        return True
    else:
        return False