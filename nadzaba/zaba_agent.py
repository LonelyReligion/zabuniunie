class zaba_agent:
    def __init__( #inicjalizacja
        self,
        #opcjonalnie listy prawdopodobienstw dla konkretnych przypadkow
        # a b c
        #1
        #2  X
        #3
        a1chances,
        a2chances,
        a3chances,
        b1chances,
        b3chances,
        c1chances,
        c2chances,
        c3chances
    ):
        self.a1chances = a1chances
        self.a2chances = a2chances
        self.a3chances = a3chances
        self.b1chances = b1chances
        self.b3chances = b3chances
        self.c1chances = c1chances
        self.c2chances = c2chances
        self.c3chances = c3chances
        self.fitness = 0 #wynik inicjalizowany 0
        pass

    def pobierz_akcje(self): #co robimy + informacje ze srodowiska
        #self.fitness jest rowny pozycji y
        return 1 #jakas akcja z najwiekszym prawdopodobienstwem