symbol = 'slkallioslklslkl'

#################################################
#################################################

# Slice the first 5 chars in stirng symbol, align to right,
# witdth of the sliced string is 12
print(f"{symbol:>12.05}")   # output: '       slkdl'

# Slice the first 5 chars in stirng symbol,
# align to left (default align to left),
# witdth of the sliced string is 12
print(f"{symbol:<12.05}")   # output: 'slkdl       '
