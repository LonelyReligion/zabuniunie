#from copy import deepcopy
import numpy as np

class zaba_agent:
    def __init__( #inicjalizacja
        self,
        #seed, #seed do stworzenia rng
        #opcjonalnie listy prawdopodobienstw dla konkretnych przypadkow SAMOCHODÓW, dla innych typów będą kolejne listy list
        # a b c d e f g 
        #1[][][][][][][]
        #2[][][][][][][]
        #3      X
        #wartości domyślne dla sierot - losowe
        #:= pozwala na przypisywanie wartości w wyrażeniach!
        #aktualizacja 21.05: Dirichlet distribution
        Chances = -1
    ):
        if(Chances == -1):
            self.Chances = sum(np.random.dirichlet(np.ones(28),size=1))
        else:
            self.Chances = Chances #konwencja, const
        self.pozycjay = 0 #fitness
        print(self.Chances);
         

    def pobierz_akcje(self, env, obserwacja): #co robimy + informacje ze srodowiska
        glosy_za = 0
        glosy_przeciw = 0
        for i, val in enumerate(obserwacja):
            #print("indeks: " + str(i) + " wartosc: " + str(val))
            if val==1:
                glosy_za += self.Chances[i*2]
                glosy_przeciw += self.Chances[i*2+1]

        #print(str(glosy_za)+"/"+str(glosy_przeciw))

        if glosy_za >= glosy_przeciw:
            return 1
        else:
            return 0  
    
    def ustaw_fitness(self, pozycjay):
        if(self.pozycjay < pozycjay):
            self.pozycjay = pozycjay
    

# algorytm genetyczny:
# fitness - pozycja y 
# selection of the fittest frogs - wybrac te z najwiekszym punktem fitness
# wariacje - zrobic crossover ich genów


# propozycja: selekcja, krzyżowanie, mutacja
# wybieramy top 10 żab na 100
# mnozymy kazda z kazda - ich wartosci w tablicach to srednie 
# 10% (ustalić eksperymentalnie) szansy na dodanie losowej wartość z zakresu od 0.05 do 0.1(ustalić eksperymentalnie)
# normalizacja wartości
