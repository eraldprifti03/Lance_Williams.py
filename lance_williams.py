import sys

#Ανοίγουμε το αρχείο που περιέχει τα δεδομένα και τα τοποθετόυμε ταξινομημένα σε μια λίστα.
filename=sys.argv[2]
list1=[]
with open (filename) as file:
    for line in file:
        list1 += line.split()

for j in range(len(list1)):
    list1[j] = [int(list1[j])]

list1.sort(reverse=False)

#Ορίζουμε τους συντελεστές ανάλογα με την μέθοδο που επιλέγουμε
i = 0
if sys.argv[1] == "single":
    ai = 1/2
    aj = 1/2
    b = 0
    c = -1/2
elif sys.argv[1] == "complete":
    ai = 1/2
    aj = 1/2
    b = 0
    c = 1/2
elif sys.argv[1] == "average":
    ai = len(list1[i]) / (len(list1[i]) + len(list1[i]))
    aj = len(list1[i]) / (len(list1[i]) + len(list1[i]))
    b = 0
    c = 0
elif sys.argv[1] == "ward":
    ai = (len(list1[i]) + len(list1[i+1])) / ((len(list1[i]) + len(list1[i+1]) + len(list1[i])))
    aj = (len(list1[i]) + len(list1[i+1])) / (len(list1[i]) + len(list1[i+1]) + len(list1[i]))
    b = -len(list1[i+1]) / (len(list1[i]) + len(list1[i+1]) + len(list1[i]))
    c = 0

#Υπολογίζουμε τις αρχικές αποστάσεις που έχουν οι συστάδες που περιέχουν μόνο ένα στοιχείο
#Ενώνουμε τις συστάδες που έχουν την μικρότερη απόσταση σε μία άλλη συστάδα και διαγράφουμε
#παράλληλα αυτές τις συστάδες που ενώσαμε
distances = []
duplicate = []
for i in range(len(list1)-1):
    distances.append(abs(list1[i][0] - list1[i+1][0]))

for i in range(len(list1)-1):
    if (distances[i]) == min(distances):
        print(f'({list1[i][0]})' + " " +f'({list1[i+1][0]})'+" "+"{:.2f}".format(float(min(distances))) + " " +f'{len(list1[i])+len(list1[i+1])}')
        list1[i].extend(list1[i+1])
        duplicate.append(list1[i+1])

for i in list1:
    if i in duplicate:
        list1.remove(i)

#Χρησιμοποιώντας τον αλγόριθμο των Lance & Williams υπολίζουμε τις νέες αποστάσεις των συστάδων που έχουμε ενώσει
#με αυτές που απομένουν.Παράλληλα ανάλογα με την αντίστοιχη μέθοδο που έχουμε επιλέξει δημιουργούμε μια νέα συστάδα
#και διαγράφουμε τις προηγούμενες μέχρι να ενωθούν όλες σε μια μεγαλύτερη τελική συστάδα
distances.clear()
while(len(list1) > 1):
    flag = False
    for i in range(len(list1)-1):
        dist = ai*abs(list1[i][0] - list1[i+1][-1]) + aj*abs(list1[i][-1] - list1[i+1][0]) + b*abs(list1[i][0] - list1[i][-1]) + c*(abs(list1[i][0]-list1[i+1][-1]) - abs(list1[i][-1]-list1[i+1][0]))
        distances.append(dist)

    for i in range(len(list1)-1):
        if (distances[i] == min(distances) and not flag):
            print( "(" + " ".join(str(x) for x in list1[i]) + ") (" + " ".join(str(x) for x in list1[i+1]) + ")"+" {:.2f}".format(float(min(distances)))+ " " + f'{len(list1[i])+len(list1[i+1])}')
            flag = True
            list1[i].extend(list1[i+1])
            duplicate.append(list1[i+1])

    for i in list1:
        if i in duplicate:
            list1.remove(i)

    distances.clear()
