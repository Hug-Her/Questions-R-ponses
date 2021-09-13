import tkinter as tk

root = tk.Tk()
root.geometry("550x300")
root.configure(bg='#306DA5')
root.iconbitmap("Logo 1.2 bis2.ico")
root.title("Questions ! Réponses ! ")

#Texte
name = tk.Label(root, text = "Prénom :",bg='#306DA5',font=(13)).place(x = 125,y = 4)
firtsname = tk.Label(root, text = "Nom :",bg='#306DA5',font=(13)).place(x = 146,y = 30)
agee = tk.Label(root, text = "Age :",bg='#306DA5',font=(13)).place(x = 150,y = 60)
datum = tk.Label(root, text = "Date de naissance :",bg='#306DA5',font=(13)).place(x = 49,y = 88)
emaill = tk.Label(root, text = "Adresse email :",bg='#306DA5',font=(13)).place(x = 76,y = 119)
numerooo = tk.Label(root, text = "Numéro de téléphone :",bg='#306DA5',font=(13)).place(x = 29,y = 147)
natiooo = tk.Label(root, text = "Nationnalité :",bg='#306DA5',font=(13)).place(x = 95,y = 175)
sexeee = tk.Label(root, text = "Civilité :",bg='#306DA5',font=(13)).place(x = 129,y = 205)

#Prénom
myEntry1 = tk.Entry(root, width=25)
myEntry1.pack(pady=5)
#Nom
myEntry2 = tk.Entry(root, width=25)
myEntry2.pack(pady=5)
#Age
myEntry3 = tk.Entry(root, width=25)
myEntry3.pack(pady=5)
#Date de naissance
myEntry4 = tk.Entry(root, width=25)
myEntry4.pack(pady=5)
#Adresse mail
myEntry5 = tk.Entry(root, width=25)
myEntry5.pack(pady=5)
#Numéro de téléphone
myEntry6 = tk.Entry(root, width=25)
myEntry6.pack(pady=5)
#Nationnalité
myEntry7 = tk.Entry(root, width=25)
myEntry7.pack(pady=5)
#Sexe
myEntry8 = tk.Entry(root, width=25)
myEntry8.pack(pady=5)

#Action bouton
def getEntry():
    #.get()
    prenom = myEntry1.get()
    nom = myEntry2.get()
    age = myEntry3.get()
    naissance = myEntry4.get()
    email = myEntry5.get()
    num = myEntry6.get()
    natio = myEntry7.get()
    sexe = myEntry8.get()
    #test
    print (prenom, nom)
    #eciture fichier
    file = open('test.txt', 'a')
    file.write(prenom)
    file.write(", ")
    file.write(nom)
    file.write(", ")
    file.write(age)
    file.write(" ans, ")
    file.write(naissance)
    file.write(", ")
    file.write(email)
    file.write(", ")
    file.write(num)
    file.write(", ")
    file.write(natio)
    file.write(", ")
    file.write(sexe)
    file.write ("\n")
    file.close()

#bouton envoyer
btn = tk.Button(root, height=1, width=10, text="Envoyer", command=getEntry)
btn.pack()

root.mainloop()