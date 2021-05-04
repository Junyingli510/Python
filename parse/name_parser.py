from nameparser import HumanName
from nameparser.config import CONSTANTS
name = HumanName("Ralf Mühlenhöver, Geschäftsführer")

print(name.title)
print(name.first)
print(name.middle)
print(name.last)

