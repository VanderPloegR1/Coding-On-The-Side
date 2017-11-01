Surname = "Lincoln"
First_name = 'Abraham'

Concatenated_name = f"President {First_name} {Surname}"

print(Concatenated_name)

Title = 'Mr. {}'

print(Title.format(Surname))
print(Title.format(First_name + ' ' + Surname))
