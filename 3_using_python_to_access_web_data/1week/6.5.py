#!/usr/bin/python3
#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

str = 'X-DSPAM-Confidence: 0.8475 '

if ':' in str:
    commapos = str.find(':')
    dspamvalue = str[commapos+1:]
    dspamvalue = float(dspamvalue)
    print(dspamvalue)
else:
    print("No comma found")
