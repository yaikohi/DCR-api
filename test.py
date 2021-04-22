import sys

print(sys.modules)
import dcr
for module in sys.modules:
    print(module)