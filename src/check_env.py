# How do I use this? Just call check_env() to see if you have the correct
# packages installed. If it returns false, it will print out what packages
# are required. If it returns true, no further action required.
#
# Do you need to add another package? This just checks the environment.yml
# for valid packages, so this checker won't break.
#
# LOGIC: Iterate through 'pip list'
# if requirements.txt is contained in pip list, then we good
#
#
#

import os

def check_env():

    ccfile = open("requirements.txt", "r")
    atPackages = False
    isHere = False
    isInstalled = True
    env_packages = []
    installed_packages = []

    for aline in ccfile:
        values = aline.split()
        env_packages.append(values[0])
    ccfile.close()

    out = []
    out = os.popen('pip3 list').read().split()

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