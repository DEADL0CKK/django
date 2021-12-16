class CompteBancaire:    
    def __init__(self, nomInit = "Dupont", soldeInit = 1000 ):
        
        self.__nom = nomInit
        self.__solde = soldeInit
    
    def depot(self,argent):
        self.__solde += argent
        return

    def retrait(self,argent):
        self.__solde -= argent
        return
        
    def affiche(self):    
        print(f"Nom : {self.__nom}/ Solde : {self.__solde} ")



compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()