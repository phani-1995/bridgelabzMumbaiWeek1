x=float(input("Enter the temperature in celcius: "))
fahrenheit = (x*9/5)+32
print('% .2f x is % 0.2f fahrenheit' % (x,fahrenheit))

y=float(input("Enter temperature in fahrenheit: "))
celcius=(y-32)*5/9
print('% .2f x is % 0.2f celcius' % (y,celcius))