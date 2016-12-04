import csv
pupils = open("pupils.txt", "r")
pupilslines = pupils.readlines()
hobbies = open("hobbies.txt", "r")
hobbieslines = hobbies.readlines()
list = csv.writer(open("list.csv", "wb"))
list.writerow(["Имя","Хобби"])
for i in range (0,len(pupils)):
 list.writerow([pupilslines[i],hobbieslines[i]])
