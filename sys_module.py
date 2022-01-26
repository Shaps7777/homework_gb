import sys
print(sys.executable)
# print(sys.platform)

import os
print(os.listdir())
os.chdir('../')
print(os.listdir())