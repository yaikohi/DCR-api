import sys

print(sys.modules)
from services.dcr import *

for module in sys.modules:
    print(module)