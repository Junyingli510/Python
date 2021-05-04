from sys import platform
if platform == "linux" or platform == "linux1" or platform == "linux2":
    # linux
    print("Your OS is linux")
elif platform == "darwin":
    # OS X
    print("Your OS is MAC OS")
elif platform == "win32":
    # Windows...
    print("Your OS is Windows")
