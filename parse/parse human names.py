from nameparser import HumanName

full_name = "Ayad Saleh Muflahi Jr"

first_name = HumanName(full_name).first
middle_name = HumanName(full_name).middle
last_name = HumanName(full_name).last
title = HumanName(full_name).title
suffix = HumanName(full_name).suffix

print(f"first_name: {first_name}")
print(f"middle_name: {middle_name}")
print(f"last_name: {last_name}")
print(f"title: {title}")
print(f"suffix: {suffix}")