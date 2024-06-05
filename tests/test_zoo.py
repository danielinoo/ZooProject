#daniele Pietropaolo

import unittest
from unittest import TestCase
from src.zoo import ZooKeeper, Zoo,Animal,Fence




class TestZoo(TestCase):

    def test_animal_dimesion(self): 

        #controllo se un animale entra nel recinto



        zookeeper_1 : ZooKeeper = ZooKeeper("gianni","rossi",23)
        fence_1 : Fence = Fence(100,25.0,"savana")
        animal_1 : Animal = Animal("pluto","canide",2,500.0,1.0,"savana")
    
        zookeeper_1.add_animal(animal_1,fence_1)
        result : int = len(fence_1.animals)

        message : str = f"Error:l'animale non entra"

        self.assertEqual(result, 0,message)


    def test_habitat(self):

        zookeeper_1 : ZooKeeper = ZooKeeper("gianni","rossi",23)
        fence_1 : Fence = Fence(100,25.0,"sea")
        animal_1 : Animal = Animal("pluto","canide",2,5.0,1.0,"savana")
    
        zookeeper_1.add_animal(animal_1,fence_1)
        result : int = len(fence_1.animals)
        
    
        message : str = f"Error: l'animale sta nell' habitat sbagliato arispostalo!"

        self.assertEqual(result, 0,message)




    def test_add_animal(self):


        zookeeper_1 : ZooKeeper = ZooKeeper("gianni","rossi",23)
        fence_1 : Fence = Fence(100,25.0,"savana")
        animal_1 : Animal = Animal("pluto","canide",2,5.0,1.0,"savana")
    
        zookeeper_1.add_animal(animal_1,fence_1)
        result : int = len(fence_1.animals)

        message : str = f"Error:l'animale nun ce entra zi"

        self.assertEqual(result, 1,message)



    def test_remove_animal(self): 
    #controllo se Remove_animal riesce a gestire un animale che non si trova dentro il recinto(e quindi non puo essere rimosso)

        zookeeper_1 : ZooKeeper = ZooKeeper("gianni","rossi",23)
        fence_1 : Fence = Fence(100,25.0,"sea")
        animal_1 : Animal = Animal("pluto","canide",2,5.0,1.0,"savana")

        zookeeper_1.remove_animal(animal_1,fence_1)

        result : int = len(fence_1.animals)


        message : str = f"Error: l'animale nun ce sta nel recinto"

        self.assertEqual(result, 0,message)


    def test_feed(self): #controllo se si puo

        zookeeper_1 : ZooKeeper = ZooKeeper("gianni","rossi",23)
        fence_1 : Fence = Fence(10,25.0,"savana")
        animal_1 : Animal = Animal("pluto","canide",2,10.0,1.0,"savana")
        zookeeper_1.add_animal(animal_1,fence_1)
        old_area = animal_1.fence.area

        zookeeper_1.feed(animal_1)
        result : int = animal_1.fence.area

        message : str = f"Error: l'animale è troppo grasso mettilo a dieta"

        self.assertEqual(result, old_area,message)




    def test_clean(self): #controllo se la funzione clean funziona anche se data un area a 0


        zookeeper_1 : ZooKeeper = ZooKeeper("gianni","rossi",23)
        fence_1 : Fence = Fence(10,25.0,"savana")
        animal_1 : Animal = Animal("pluto","canide",2,5.0,2.0,"savana")
    
        result : int = zookeeper_1.clean(fence_1)
        
    
        message : str = f"ERRORE"

        self.assertEqual(result, 0,message)


    




    

        





    






















