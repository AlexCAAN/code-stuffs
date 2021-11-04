def pretty_price(oprice, extension):
    if isinstance(extension, int):
        extension = extension * 0.01


    return int(oprice) + extension


print(pretty_price(7.25, 0.37))
print(pretty_price(7.25, 37))