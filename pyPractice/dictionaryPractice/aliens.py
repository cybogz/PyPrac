#Make an empty list to store aliens
aliens = []

#create 30 alien dictionaries and append it to the aliens list
for alienNumber in range(30):
    alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(alien)

for changeColor in aliens[0:3]:
    if changeColor['color'] == 'green':
        changeColor['color'] = 'yellow'
        changeColor['points'] = 10
        changeColor['speed'] = 'medium'

#show the first 5 aliens
for displayAlien in aliens[:5]:
    print(displayAlien)
print("...")

#show how many aliens are in the list
print("Total number of aliens: " + str(len(aliens)))