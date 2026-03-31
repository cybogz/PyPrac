aliens = []

# Make 30 aliens

for alienNumber in range(30):
    newAlien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(newAlien)

# Change some to yellow aliens

for yellowAliens in aliens[0:3]:
    if yellowAliens['color'] == 'green':
        yellowAliens['color'] = 'yellow'
        yellowAliens['speed'] = 'medium'
        yellowAliens['points'] = 10

# Show aliens

for alien in aliens[0:5]:
    print(alien)
print('...')

# Show how many aliens are on the list

print("Total number of aliens: " + str(len(aliens)))