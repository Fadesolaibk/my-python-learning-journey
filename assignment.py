m = 'you are welcome'

#capitalize
modified = m.capitalize()#capitalizing the first word
print('message:', m)
print('modified:', modified)

#count
n = m.count('o')
print('no of occurence of "o":', n)

#endswith
print(m.endswith('e'))
print(m.endswith('a'))

#find
print("index of 'w':", m.find('w'))

#index
print('index of w: ', m.index('w'))

o = 'fadesola123'
#isalnum
print(m.isalnum())

#isalpha
print(m.isalpha())

o = 'fadesola123'
#isalnum
print(o.isalnum())

#isalpha
print(o.isalpha())

#isdecimal
p = "123456"
print(p.isdecimal())

#isdigit
print(p.isdigit())
print(o.isdigit())

#islower
print(o.islower())
print(p.islower())

#isnumeric
print(o.isnumeric())
print(p.isnumeric())

q = '   '
r = "Ibukun Billions"
s = "BILL GATES"
t = ['warren', 'buffet']
#isspace
print(o.isspace())
print(q.isspace())

#istitle
print(o.istitle())
print(r.istitle())

#isupper
print(r.isupper())
print(s.isupper())

#join
sep = '-'
print(sep.join(r))
print(sep.join(t))

#lower
print(s.lower())

u = '    ibukun     '
#lstrip
print(u.lstrip())

#replace
print(r.replace('ibukun','fortune'))
print(r)

#rfind
print('index of G: ', s.rfind('G'))
print('index of L: ', s.rfind('L'))

#rindex
print('index of n: ', r.rindex('n'))
print('index of u: ', r.rindex('u'))

#rstrip
print(u.rstrip('n'))
print(m.rstrip('welcome'))

#rsplit
print(m.rsplit(' '))

#split
print(m.split(' '))

#startswith
print(m.startswith('you'))
print(m.startswith('are'))

#strip

#swapcase

#title

#upper
