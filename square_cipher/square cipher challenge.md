# The Square Cipher Challenge

## What is a square cipher?
As challenge problem, try and build a square cipher. A square cipher is an old way of encoding a string of text so that it can only be read by someone who has the key. Here's how it works:

* Take a phrase
"This is cat"

* Write the phrase as a rectangle. Here we leave out spaces, but you could leave them in.\s\s
Thi\s\s
sis\s\s
cat\s\s

* The encoded text is now the string if you read down the box instead of across:
Tschiaist

* To decode, you have to know the number of rows (in this case, 3). You would write it out like the box above, writing down first and then reading left to right. This would produce the phrase:
Thisiscat

## The Task
This process can be accomplishing using only techniques that we have learned so far. With that in mind, write a script called square_cipher.py to encode and decode the following phrase:

"A journey of a thousand miles begins with a single step"

* Use 5 rows in the cipher (the phrase is 55 characters long with spaces included, 50 without)
* Try to design it in a way that your cipher can encode or decode ANY phrase evenly divisable by 5. Next class we can test a few ciphers on other phrases!

## Hint!
The phrase itself might contain a clue as to how to approach the problem....
