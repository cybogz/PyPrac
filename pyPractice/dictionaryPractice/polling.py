favLanguage = {'cyrus': 'python',
               'bob': 'c++',
               'stavi': 'javascript'}

peopleListed = ['cyrus', 'javy', 'stavi']

for person in peopleListed:
    if person in favLanguage :
        print(person + " thanks for submitting your favorite language")
    else:
        print(person + " would you like to submit a favorite language")