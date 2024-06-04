import gymnasium as gym
import numpy as np #moze do generowania seeda?
import zaba_agent
import random
import pickle

DEBUG = False
WCZYTUJEMY = False

def szukajaut(obs, pixel_x, pixel_y):
    # a b c d e f g 
    #1[][][][][][][]
    #2[][][][][][][]
    #3      X
    a1 = b1 = c1 = d1 = e1 = f1 = g1 = a2 = b2 = c2 = d2 = e2 = f2 = g2 = 0
    
    slepota = 1
    if(pixel_y==161 or pixel_y==122):
        slepota=0
    
    if(slepota):
        #góra góra lewo lewo lewo
        for linijka in range(pixel_y-14, pixel_y-7): #wysokosc zaby
            for pixel in range(pixel_x-21, pixel_x-14): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry góry, z lewej lewej lewej!")
                        a1 = 1
        
        #góra góra lewo lewo
        for linijka in range(pixel_y-14, pixel_y-7): #wysokosc zaby
            for pixel in range(pixel_x-14, pixel_x-7): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry góry, z lewej lewej!")
                        b1 = 1
        
        #góra góra lewo
        for linijka in range(pixel_y-14, pixel_y-7): #wysokosc zaby
            for pixel in range(pixel_x-7, pixel_x): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry góry, z lewej!")
                        c1 = 1
        #góra prawo
        for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
            for pixel in range(pixel_x+7, pixel_x+14): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry prawo!")
                        e2 = 1
        
        #góra prawo prawo
        for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
            for pixel in range(pixel_x+14, pixel_x+21): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry prawo prawo!")
                        f2 = 1
        
        #góra prawo prawo prawo
        for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
            for pixel in range(pixel_x+21, pixel_x+28): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry prawo prawo prawo!")
                        g2 = 1
    else:
         #góra lewo lewo lewo
        for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
            for pixel in range(pixel_x-21, pixel_x-14): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry, z lewej lewej lewej!")
                        a2 = 1 
        
        #góra lewo lewo
        for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
            for pixel in range(pixel_x-14, pixel_x-7): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry, z lewej lewej!")
                        b2 = 1
        
        #góra lewo
        for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
            for pixel in range(pixel_x-7, pixel_x): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry, z lewej!")
                        c2 = 1 
        #góra góra prawo
        for linijka in range(pixel_y-14, pixel_y-7): #wysokosc zaby
            for pixel in range(pixel_x+7, pixel_x+14): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry góry prawo!")
                        e1 = 1 
        
        #góra góra prawo prawo
        for linijka in range(pixel_y-14, pixel_y-7): #wysokosc zaby
            for pixel in range(pixel_x+14, pixel_x+21): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry góry prawo prawo!")
                        f1 = 1 
        
        #góra góra prawo prawo prawo
        for linijka in range(pixel_y-14, pixel_y-7): #wysokosc zaby
            for pixel in range(pixel_x+21, pixel_x+28): #szerokosc zaby
                #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
                if((obs[linijka][pixel]!=[0, 0, 0]).all() and
                (obs[linijka][pixel]!=[232, 233,74]).all()):
                        if(DEBUG): print("Auto od góry góry prawo prawo prawo!")
                        g1 = 1
    
    #sprawdzenie dla wszystkich
    #góra góra
    for linijka in range(pixel_y-14, pixel_y-7): #wysokosc zaby
        for pixel in range(pixel_x, pixel_x+7): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]!=[0, 0, 0]).all() and
               (obs[linijka][pixel]!=[232, 233,74]).all()):
                    if(DEBUG): print("Auto od góry góry!")
                    d1 = 1
     
    #góra
    for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
        for pixel in range(pixel_x, pixel_x+7): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]!=[0, 0, 0]).all() and
               (obs[linijka][pixel]!=[232, 233,74]).all()):
                    if(DEBUG): print("Auto od góry!")
                    d2 = 1
    
    return [a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2]; 

def znajdz_zabe(obs, zaba):  #optymalizacja: w pixel_x i pixel_y mamy przednia lewa lapke!!!
    #idziemy od dołu?
    pixel_x = 0
    pixel_y = 0

    for linijka in obs:
        pixel_x = 0
        for pixel in linijka:
            if((pixel==[110, 156, 66]).all()):
                return [pixel_x, pixel_y]
            pixel_x+=1
        pixel_y+=1

def crossover(zaby, mutation_rate=0.1, mutation_scale=0.05):
    new_population = []
    
    zaby = sorted(zaby, key=lambda x: x.pozycjay, reverse=True) # Sortujemy żab według fitness w malejącej kolejności
    
   
    top_zaby = zaby[:4] # Narazie top 4 najlepszych 
    nad_zaba = zaby[0]

    open("nadzaba.pkl", "w").close()
    # Zapisujemy zabki do pliku
    with open('nadzaba.pkl', 'wb') as file:
        pickle.dump(nad_zaba, file)

    # Tworzenie nowych żab poprzez mieszanie genów
    for i in range(len(top_zaby)):
        for j in range(len(top_zaby)):
            if(len(new_population)>=10):
                return new_population
            if(i != j):
                parent1 = top_zaby[i]
                parent2 = top_zaby[j]
                
                new_genes = (parent1.Chances + parent2.Chances) / 2 #Srednia z genów rodzicow
                
                if(random.random() >= 0.9): #10% szansa float
                    new_genes[random.randrange(27)] += 0.1; #0 do 27  int
                
                new_genes = new_genes/sum(new_genes) # I trzeba moze znormalizować dane
                # Mozemy tu stworzyc jakas mutacje genow lub utworzyc do tego inna funkcje ale nie wiem co ile zab powinnysmy cos mutowac
                # Tworzenie nowej żaby z nowymi genami
                new_zaba = zaba_agent.zaba_agent()
                new_zaba.Chances = new_genes
                new_population.append(new_zaba)
    

def run():
    env = gym.make("ALE/Frogger-v5", render_mode="human", obs_type="rgb")
    #render_module: human, rgb_array, ansi, rgb_array_list, ansi_list 
    print(env.observation_space)
    obs, info = env.reset()
    terminated = False
    truncated = False
    # kolor ramki: [82, 126, 45]
    # kolor żaby: [110, 156, 66]
    # kolory aut: fioletowe [164, 89, 208], różowe [198, 89, 179], zielone [82, 126, 45], 
    # pomarańczowe [195, 144, 61], białe [236,136,136]
    # kolory liści: brązowe [144, 72, 17], niebieskie [66, 114, 194]
    # kolory kłód: [105, 105, 15]

    # 13 wysokosc
    # 8 + 1 + 8 = 19 szerokosc
    i = 0
    pokolenie = 1

    if(WCZYTUJEMY):
             # sprawdzenie, tak bedziemy ja wczytywac na prezentacji
        with open('nadzaba.pkl', 'rb') as file:
            zabcia = pickle.load(file)
    else:
        zabcia = zaba_agent.zaba_agent()
    zabcie = []
    nowe_lepsze_zabcie = []

    while(True):
        zaba_x, zaba_y = znajdz_zabe(obs, zabcia)
        zabcia.ustaw_fitness(zaba_y)
        if(not terminated and not truncated): #na potrzeby testu, jedna zaba do smierci lub znudzenia;)
            i+=1
            if i % 6 <= 3:
                action = zabcia.pobierz_akcje(env, szukajaut(obs, zaba_x, zaba_y))
            else:
                #konieczne, poniewaz symulujemy przyciski - jesli akcja sie powtorzy zostanie wykonanana tylko raz 
                #mogloby to zaburzyc proces uczenia sie imo
                
                action = 0
            obs, reward, terminated, truncated, info = env.step(action)
        else:
            print(f"Kolejna żaba zakończyła żywot. Fitness: {zabcia.pozycjay}.")
            if(WCZYTUJEMY):
                env.reset()
                env.close()
                exit(0)
            zabcie.append(zabcia)
            if(int(len(zabcie))>=10):
                
                #dokonujemy selekcji
                nowe_lepsze_zabcie = crossover(zabcie, mutation_rate=0.1, mutation_scale=0.05) #tworzymy tablice z nowymi lepszymi 5 zabciami
                zabcie = [];
                pokolenie=pokolenie+1
                print("Pokolenie "+ str(pokolenie) + ". ")
            else:
                print("Spawnuję "+str(len(zabcie)+1)+". żabę")
                if(len(nowe_lepsze_zabcie) != 0):
                    zabcia = nowe_lepsze_zabcie[len(zabcie)];
                else:
                    zabcia = zaba_agent.zaba_agent()

            obs, info = env.reset()
            terminated = False
            truncated = False
    

if __name__ == '__main__':
    run()