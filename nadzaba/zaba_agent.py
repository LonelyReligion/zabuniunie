import random

class zaba_agent:
    def __init__( #inicjalizacja
        self,
        #seed, #seed do stworzenia rng
        #opcjonalnie listy prawdopodobienstw dla konkretnych przypadkow
        # a b c
        #1
        #2  X
        #3
        chances = [
            #a1
            [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), #wartości domyślne dla sierot - losowe
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d], #:= pozwala na przypisywanie wartości w wyrażeniach!
            #a2
            [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
            #a3
            [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
            #b1
            [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
            #b3
            [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
            #c1
            [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
            #c2
            [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
            #c3
            [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d]
        ]
    ):
        #random.seed(seed) #to powinno byc uzyte w zabcia = zaba_agent.zaba_agent(seed=seed) ?
        # w seedzie mozemy przechowywac ruchy danej żaby

        self.chances = chances

        self.pozycjax = 8
        self.pozycjay = 0

        self.fitness = 0 #wynik inicjowany 0
        
        pass

    def pobierz_akcje(self, env, obserwacja): #co robimy + informacje ze srodowiska
        #self.fitness jest rowny pozycji y
        self.fitness = self.pozycjay
        #rozpoznajemy akcje
        noEvent = 1
        print("Zarejestrowano zdarzenie " + str(noEvent) + "\n" + str(self.chances[noEvent]))
        if(noEvent > len(self.chances)-1):
            return env.action_space.sample()
        #kumulowanie prawdopodobienstwa
        skumulowane = self.chances.copy() #pamietaj domyslnie kopiuje sie ;) wskazniki
        for i in range(0, len(skumulowane[noEvent]) - 1): #dla kazdego kierunku
            skumulowane[i] = self.chances[i].copy() #pamietaj domyslnie kopiuje sie ;) wskazniki
            if(i == 0):
                pass
            else:
                skumulowane[noEvent][i] = skumulowane[noEvent][i] + skumulowane[noEvent][i-1]

        #losujemy akcje
        wylosowana_wartosc = random.random()
        for i in range(0, len(skumulowane[noEvent]) - 1): #dla kazdego kierunku
            if(wylosowana_wartosc <= skumulowane[noEvent][i]):
                print("Wylosowano akcje " + str(i))
                #jezeli akcja to pojscie w gore to wynik++
                #jezeli w dol to pojscie w dol
                return i


        return 3 #jakas akcja z najwiekszym prawdopodobienstwem
    

# algorytm genetyczny:
# fitness - pozycja y 
# selection of the fittest frogs - wybrac te z najwiekszym punktem fitness
# wariacje - zrobic crossover ich genów

# TODO
# !analiza obrazu!, seedy
