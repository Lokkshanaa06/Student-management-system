import os
path="Lokkshanaa"
if os.path.exists(path):
    print("The path exists")
else:
    print("The path does not exist")
    os.mkdir(path)
    print("The path created ")