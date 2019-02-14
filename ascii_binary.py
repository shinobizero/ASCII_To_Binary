# -*- coding: utf-8 -*-

print('Ascii To Binary Converter')
text_input = input('Please enter text to convert: ')

bin_list = []
dec_list = []

#Convert --> Decimal
for char in text_input:
    dec_list.append(ord(char))
#Calculate Decimal -- > Bianry Remainders
for decimal in dec_list:
    binary = ''
    while decimal > 0:
        if decimal % 2 == 0:
            binary = binary + str(0)
        else:
            binary = binary + str(1)
        decimal = decimal//2
    #Add padding 0's to make 8 bit
    if len(binary) < 8:
        binary_padding = str(0)*(8-len(binary))
        full_binary = binary + binary_padding + ' '
    else:
        full_binary = binary + ' '
    #Reverse Binary String For It To Be Correct
    bin_list.append(full_binary[::-1])
bin_seq = ''
for digit in bin_list:
    bin_seq += str(digit)
print(text_input, '=')
print(bin_seq)