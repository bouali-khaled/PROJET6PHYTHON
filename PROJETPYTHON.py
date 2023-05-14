import sys
import tkinter as tk



class Comptebancaire:
    def __init__(self, proprietaire,numcompte,solde) :
        self.proprietaire = proprietaire
        self.numcompte = numcompte
        self.solde = solde

    def ajouter (self, sommeAjouter):
        self.solde += sommeAjouter
        print(f"votre nouveau solde est de : {self.solde}")

    def retirer (self,sommeRetirer):
        if (self.solde>=sommeRetirer):
            self.solde -= sommeRetirer
        else :
            print("votre solde est inferieure!!")

    def afficher(self):
        print(f"Mr :{self.proprietaire}")
        print(f"numero de compte est le :{self.numcompte}")
        print(f"le solde du compte est de :  {self.solde}   Euros")

    

class CompteBancaireGUI:
    def __init__(self, master, compte):
        self.master = master
        self.compte = compte

        # Titre et geometry  DE la fenetre 

        self.master.title("Gestion de Compte Bancaire")
        self.master.geometry("500x500")

        # afficher le proprietaire  du compte 
        self.label_proprietaire = tk.Label(self.master, text=f"Propriétaire du compte est : {self.compte.proprietaire}")
        self.label_proprietaire.pack()

        #  afficher le numcompte 
        self.label_num = tk.Label(self.master, text=f"Numéro de compte est : {self.compte.numcompte}")
        self.label_num.pack()

        #  afficher le solde du compte 
        self.label_solde = tk.Label(self.master, text=f"Solde est de : {self.compte.solde} euros")
        self.label_solde.pack()

        # affichr  transactions 
        self.label_transaction = tk.Label(self.master, text="transactions:")
        self.label_transaction.pack()

        #ajouter u champs pour entrer la somme (pour ajouter ou retirer)
        self.entry_transaction = tk.Entry(self.master)
        self.entry_transaction.pack()

        #ajouter un button ajouter  une somme
        self.button_ajouter = tk.Button(self.master, text="Ajouter une  somme", command=self.ajouter)
        self.button_ajouter.pack()

        #ajouter un button retirer une  somme
        self.button_retirer = tk.Button(self.master, text="Retirer une somme", command=self.retirer)
        self.button_retirer.pack()

        #ajouter un button retirer une  somme
        self.button_quit= tk.Button(self.master, text="quit", command=self.quit)
        self.button_quit.pack()


    def ajouter(self):
        
            somme = float(self.entry_transaction.get())
            self.compte.ajouter(somme)
            self.label_solde.config(text=f"Solde: {self.compte.solde} €")# pour afficher le solde final apres avoir ajouter une somme
        

    def retirer(self):
        
            somme = float(self.entry_transaction.get())
            self.compte.retirer(somme)
            self.label_solde.config(text=f"Solde: {self.compte.solde} euros")

    def quit(self):
         sys.exit()
        

        

compte = Comptebancaire("cristoph ", "123MB0", 2000)# instanciation d 'un compte dans comptebancaire 
root = tk.Tk()# fenetre principale 
gui = CompteBancaireGUI(root, compte)#interface pour le comptebancaire
root.mainloop()#demarage de l interface



