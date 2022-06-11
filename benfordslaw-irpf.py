import re
import matplotlib.pyplot as plt

file = open("irpf.xml", "r")
irpf = file.read()

# this pattern find money values, basically it searches for numbers that are terminated with commas and two decimal places
pattern = '[0-9]*\.?[0-9]*,[0-9]{2}"'
# this pattern can't recognize million, but it doesn't a my use case, unfortunately. 

# find patten on irpf.xml file
occurrence = re.findall(pattern, irpf)
qty_occurrence = len(occurrence)

# now we get first digit and save as integer
first_digit = []
for i in occurrence:
    if i[0] != '0':
        str2int = int(i[0])
        first_digit.append(str2int)
qty_first_digit = len(first_digit)
# sort list to easy count
first_digit.sort()

# in this point we start count first digit occurrence
count = {}
for i in first_digit:
    count[i] = first_digit.count(i)

# Show result on terminal:
print ('# First digit and frequency:')
for key,value in count.items():
    print(key, ':', value)

print ( 'Amount of values analysed: ', qty_occurrence )
print ( 'Amount of valid values(no zero): ', qty_first_digit )
print ( '\nGenerating chart...')

# preparing the chart
# the values in 'count' dict will be used are prepared for X and Y axes
x = []
y = []
for key,value in count.items():
    x.append(key)
    y.append(value)

plt.plot(x, y, linewidth = 2, marker='o')
plt.xlabel('first digit')
plt.ylabel('frequency')

plt.title('Using Benford\'s Law on IRPF(Brazilian Personal Income Tax')

# let's plot the graph!
plt.savefig('BenfordsLaw-analysis-on-IRPF.png')
print( 'Chart saved Benford-analysis-on-IRPF.png' )

