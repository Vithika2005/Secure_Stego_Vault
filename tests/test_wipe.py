from storage.secure_delete import secure_delete

# create dummy file
with open("data/test.txt", "w") as f:
    f.write("TOP SECRET")

secure_delete("data/test.txt")

import os
print("Exists:", os.path.exists("data/test.txt"))
