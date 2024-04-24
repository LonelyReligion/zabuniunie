import random

class zaba_agent:
    def __init__( #inicjalizacja
        self,
        #opcjonalnie listy prawdopodobienstw dla konkretnych przypadkow
        # a b c
        #1
        #2  X
        #3
        a1chances = [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), #wartości domyślne dla sierot - losowe
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d], #:= pozwala na przypisywanie wartości w wyrażeniach!
        a2chances = [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
        a3chances = [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
        b1chances = [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
        b3chances = [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
        c1chances = [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
        c2chances = [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d],
        c3chances = [a := random.random(), b:= random.uniform(0.0, 1-a), c:= random.uniform(0.0, 1-a-b), 
                     d:= random.uniform(0.0, 1-a-b-c), 1-a-b-c-d]
    ):
        self.a1chances = a1chances
        self.a2chances = a2chances
        self.a3chances = a3chances
        self.b1chances = b1chances
        self.b3chances = b3chances
        self.c1chances = c1chances
        self.c2chances = c2chances
        self.c3chances = c3chances

        self.fitness = 0 #wynik inicjowany 0
        pass

    def pobierz_akcje(self, obserwacja): #co robimy + informacje ze srodowiska
        #self.fitness jest rowny pozycji y
        return 1 #jakas akcja z najwiekszym prawdopodobienstwem