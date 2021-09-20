import importlib.util
import sys

def check_env():

    print("REQUIRED ENV PACKAGES")

    ccfile = open("environment.yml", "r")
    atPackages = False
    env_packages = []

    for aline in ccfile:
        values = aline.split()
        if(atPackages == True):
            env_packages.append(values[1])
            print(values[1])
        if(values[0] == "dependencies:"):
            atPackages = True

    ccfile.close()
    print("ENV PACKAGE STATUS")
    for name in env_packages:
        if "=" in name:
            terminator = name.index('=')
            name = name[:terminator]
        if (spec := importlib.util.find_spec(name)) is not None:
            print(F"{name!r} exists")
        else:
            print(f"can't find the {name!r} module")

check_env()