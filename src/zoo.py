#daniele pietropaolo
#16/05/24


#-------------------------------#

class Animal:

    def __init__(self,name : str,species: str,eta : int,height : float,width : float,prefer_habitat : str):

        self.name = name
        self.species = species
        self.age = eta
        self.height = height
        self.width = width
        self.prefer_habitat = prefer_habitat

        self.fence : Fence = None #varabile di supporto che "collega Animal e Fence"
        self.health = round(100 * (1 /self.age), 3)



#-------------------------------#

class Fence:
    def __init__(self,area : float,temperature :float,habitat : str):

        self.animals : list[Animal] = []
        
        self.temperature = temperature
        self.habitat = habitat
        self.area = area
        if area < 0:
            self.area = 0
            





#-------------------------------#



class ZooKeeper:


    
    def __init__(self,name : str,surname : str,id : str):

        self.name = name
        self.surname = surname
        self.id = id
        




    def add_animal(self,animal: Animal, fence: Fence):

        if animal.prefer_habitat != fence.habitat or fence.area < animal.height*animal.width:
            pass
            
        
        else: 
            #lista degli animali del recinto aggiunge un nuovo animale
            fence.animals.append(animal)

            #sottraggo all' area del recinto l'area del nuovo animale
            fence.area = fence.area - (animal.height * animal.width)
            animal.fence = fence

    




    def remove_animal(self,animal: Animal, fence: Fence):


        if not fence.animals :
            pass

        else:
            #lista degli animali del recinto rimuove l animale
            fence.animals.remove(animal)

            #aggiungo all'area del recinto l'area dell'animale appena uscito
            fence.area = fence.area + (animal.height*animal.width)



    

    def feed(self,animal: Animal):


        if animal.fence != None:

            if animal.fence.area >= animal.height * animal.width:

            #variabili di appoggio
                h : float = animal.height
                w : float = animal.width

        #aumento salute animale del 1%
                animal.health = animal.health * 1.01

        #aumento altezza e larghezza del 2%
                animal.height = animal.height * 1.02
                animal.width = animal.width * 1.02
            
                if animal.fence.area < animal.height * animal.width:

                #sedopo averlo nutrito l' animale è troppo grande gli ritornano i valori iniziali
                    animal.height = h
                    animal.width = w
                
                else: #aggiorno l area del recinto
                    animal.fence.area = animal.fence.area - (animal.height * animal.width)

                
            else:
                pass

        else: 
            pass
        
        

    def clean(self,fence: Fence) -> float:



        #area occupata dagli animali
        area_animali : float = 0
        
        for animal in fence.animals:
            area_animali += animal.height * animal.width

        if fence.area == 0:
            return area_animali

        return area_animali / fence.area



class Zoo:
    def __init__(self,fences : list[Fence],zoo_keepers : list[ZooKeeper]):

        self.fence = fences
        self.zoo_keepers = zoo_keepers


    def describe_zoo(self):

        print("\nGuardians:\n")

        for i in self.zoo_keepers:
            print(f"ZooKeeper(name={i.name},surname={i.surname},id={i.id})\n")

        for i in self.fence:
            print("Fence:\n")
            print(f"Fence(area={i.area},temperature={i.temperature},habitat={i.habitat})\n")
            print("with animals\n")

            for j in i.animals:

                print(f"Animal(name={j.name},species={j.species},age={j.age})\n")

            print("#" * 30,"\n")
