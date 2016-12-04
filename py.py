import csv
pupils = open("pupils.txt", "r")
pupilslines = pupils.readlines()
hobbies = open("hobbies.txt", "r")
hobbieslines = hobbies.readlines()
with open('names.csv', 'w') as csvfile:
    fieldnames = ['Name', 'Hobby']
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i in range (0,len(pupilslines)):
        writer.writerow({'Name': pupilslines[i] , 'Hobby':hobbieslines[i]})

