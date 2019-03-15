#! /usr/bin/env python3

#### measure string, adjust it to the right size, 5 rows tall, n columns long
phrase = 'A journey of a thousand miles begins with a single step'
rows = 5
print('input is {} characters'.format(len(phrase)))

## these are handy to have later on.
lphrase = len(phrase)
cols = int(lphrase / rows) # how many columns


####### encoding
## gather elements at intervals
encoded = ''
for column in range(cols):
    for idx in range(int(lphrase / cols)):
        encoded += phrase[(idx * cols)+column]
print(encoded)


####### decoding
## split into smaller strings
snipit = ''
boxes = []

for i in range(lphrase):
    if (i % 5 == 0) and (i != 0):
        boxes.append(snipit)
        snipit = ''
    snipit += encoded[i]
else:
    boxes.append(snipit)

## add the elements together based on index
decoded = ''
for idx in range(rows):
    for snipit in boxes:
        decoded += snipit[idx]
print(decoded)