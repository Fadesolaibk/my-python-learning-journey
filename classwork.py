name = input('please enter your name:',)
print('welcome,', name) 
print('please enter your score:')
score = int(input())
if score >= 70:
    print (name,'`s score is:', score, 'hence he gets an A')
if score >=60 and score< 70:
    print (name,'`s score is:', score, 'hence he gets a B')
if score >=55 and score< 60:
    print (name,'`s score is:', score, 'hence he gets a C')
if score >=50 and score< 55:
    print (name,'`s score is:', score, 'hence he gets a D')
if score >=45 and score< 50:
    print (name,'`s score is:', score, 'hence he gets an E')
if score < 45:
    print (name,'`s score is:', score, 'hence he gets an F')

