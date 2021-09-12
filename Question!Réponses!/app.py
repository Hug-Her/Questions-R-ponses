import tkinter as tk

root = tk.Tk()
root.geometry("550x500")
root.configure(bg='#306DA5')
root.iconbitmap("Logo 1.2 bis2.ico")
root.title("Questions ! Réponses ! ")

name = tk.Label(root, text = "Prénom :",bg='#306DA5',font=(13)).place(x = 125,y = 54)

myEntry1 = tk.Entry(root, width=25)
myEntry1.pack(pady=56)



def getEntry():
    prenom = myEntry1.get()
    print (prenom)
    file = open('test.txt', 'a')
    file.write(prenom)
    file.write ("\n")
    file.close()


btn = tk.Button(root, height=1, width=10, text="Envoyer", command=getEntry)
btn.pack()





root.mainloop()