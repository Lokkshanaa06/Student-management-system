string1="a gentle breeze whispered through the ancient trees."
string2="He had had enough of their endless, endless arguments."
string3="banana"
string4="TOMORROW IS A BIG DAY."
string5="he\tll\to"
string6="hulk50"

print("\nCapitalize function:")
mod_str=string1.capitalize()
print(mod_str)

print("\nCasefold function:")
mod_str=string4.casefold()
print(mod_str)

print("\nCenter function:")
mod_str=string3.center(20)
print(mod_str)

print("\nCount function:")
x=string2.count("endless")
print(x)

print("\Encode function:")
mod_str=string1.encode()
print(mod_str)

print("\nEndswith function:")
mod_str=string1.endswith(".")
print(mod_str)
mod_str=string1.endswith(",")
print(mod_str)

print("\nExpandtabs function:")
mod_str=string5.expandtabs(4)
print(mod_str)

print("\nFind function:")
x=string2.find("had")
print(x)

print("\nFormat function:")
txt1="my name is {} and my age is {}".format("lokkshanaa",20)
txt2="my name is {name} and my age is {age}".format(name="lokkshanaa",age=20)
txt3="my name is {0} and my age is {1}".format("lokkshanaa",20)
print(txt1)
print(txt2)
print(txt3)

print("\nIndex function:")
z=string1.index("whispered")
print(z)

print("\nAlphaumeric function:")
print(string6.isalnum())

print("\nAlp")
