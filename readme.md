This is a input based extended hamming encoder built in python. Was built to pass a level on bitburner game (level details below)


HammingCodes: Integer to Encoded Binary
You are attempting to solve a Coding Contract. You have 10 tries remaining, after which the contract will self-destruct.


You are given the following decimal value:
6732

Convert it to a binary representation and encode it as an 'extended Hamming code'.
The number should be converted to a string of '0' and '1' with no leading zeroes.
Parity bits are inserted at positions 0 and 2^N.
Parity bits are used to make the total number of '1' bits in a given set of data even.
The parity bit at position 0 considers all bits including parity bits.
Each parity bit at position 2^N alternately considers N bits then ignores N bits, starting at position 2^N.
The endianness of the parity bits is reversed compared to the endianness of the data bits:
Data bits are encoded most significant bit first and the parity bits encoded least significant bit first.
The parity bit at position 0 is set last.

Examples:
8 in binary is 1000, and encodes to 11110000 (pppdpddd - where p is a parity bit and d is a data bit)
21 in binary is 10101, and encodes to 1001101011 (pppdpdddpd)