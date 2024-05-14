import gymnasium as gym
import numpy #moze do generowania seeda?
import zaba_agent

def szukajaut(obs, pixel_x, pixel_y):
    #góra lewo
    for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
        for pixel in range(pixel_x-7, pixel_x): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]==[164, 89, 208]).all() or
               (obs[linijka][pixel]==[198, 89, 179]).all() or
               (obs[linijka][pixel]==[82, 126, 45]).all()  or
               (obs[linijka][pixel]==[195, 144, 61]).all() or
               (obs[linijka][pixel]==[236,136,136]).all()
                ):
                    print("Auto od góry, z lewej!");
                    return 0;  
    #lewo
    for linijka in range(pixel_y, pixel_y+7): #wysokosc zaby
        for pixel in range(pixel_x-7, pixel_x): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]==[164, 89, 208]).all() or
               (obs[linijka][pixel]==[198, 89, 179]).all() or
               (obs[linijka][pixel]==[82, 126, 45]).all()  or
               (obs[linijka][pixel]==[195, 144, 61]).all() or
               (obs[linijka][pixel]==[236,136,136]).all()
                ):
                    print("Auto z lewej!");
                    return 1;
    #dół lewo
    for linijka in range(pixel_y+7, pixel_y+14): #wysokosc zaby
        for pixel in range(pixel_x-7, pixel_x): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]==[164, 89, 208]).all() or
               (obs[linijka][pixel]==[198, 89, 179]).all() or
               (obs[linijka][pixel]==[82, 126, 45]).all() and pixel_x > 79 or
               (obs[linijka][pixel]==[195, 144, 61]).all() or
               (obs[linijka][pixel]==[236,136,136]).all()
                ):
                    print("Auto od dołu, z lewej!!");
                    return 2;  
    #góra
    for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
        for pixel in range(pixel_x, pixel_x+7): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]==[164, 89, 208]).all() or
               (obs[linijka][pixel]==[198, 89, 179]).all() or
               (obs[linijka][pixel]==[82, 126, 45]).all()  or
               (obs[linijka][pixel]==[195, 144, 61]).all() or
               (obs[linijka][pixel]==[236,136,136]).all()
                ):
                    print("Auto od góry!");
                    return 3;  
    #dół
    for linijka in range(pixel_y+7, pixel_y+14): #wysokosc zaby
        for pixel in range(pixel_x, pixel_x+7): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]==[164, 89, 208]).all() or
               (obs[linijka][pixel]==[198, 89, 179]).all() or
               (obs[linijka][pixel]==[82, 126, 45]).all() and pixel_x > 79 or
               (obs[linijka][pixel]==[195, 144, 61]).all() or
               (obs[linijka][pixel]==[236,136,136]).all()
                ):
                    print("Auto od dołu!");
                    return 4;  
    #góra prawo
    for linijka in range(pixel_y-7, pixel_y): #wysokosc zaby
        for pixel in range(pixel_x+7, pixel_x+14): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]==[164, 89, 208]).all() or
               (obs[linijka][pixel]==[198, 89, 179]).all() or
               (obs[linijka][pixel]==[82, 126, 45]).all()  or
               (obs[linijka][pixel]==[195, 144, 61]).all() or
               (obs[linijka][pixel]==[236,136,136]).all()
                ):
                    print("Auto od góry prawo!");
                    return 5;  
    #prawo
    for linijka in range(pixel_y, pixel_y+7): #wysokosc zaby
        for pixel in range(pixel_x, pixel_x+7): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]==[164, 89, 208]).all() or
               (obs[linijka][pixel]==[198, 89, 179]).all() or
               (obs[linijka][pixel]==[82, 126, 45]).all()  or
               (obs[linijka][pixel]==[195, 144, 61]).all() or
               (obs[linijka][pixel]==[236,136,136]).all()
                ):
                    print("Auto z prawej!");
                    return 6;  
    #prawo dół
    for linijka in range(pixel_y+7, pixel_y+14): #wysokosc zaby
        for pixel in range(pixel_x, pixel_x+7): #szerokosc zaby
            #nie musimy sprawdzac krawedzi bo mamy margines bezpieczenstwa z ramki!
            if((obs[linijka][pixel]==[164, 89, 208]).all() or
               (obs[linijka][pixel]==[198, 89, 179]).all() or
               (obs[linijka][pixel]==[82, 126, 45]).all() and pixel_x > 79 or
               (obs[linijka][pixel]==[195, 144, 61]).all() or
               (obs[linijka][pixel]==[236,136,136]).all()
                ):
                    print("Auto z dołu prawej!");
                    return 7;  
    
    return 5; #do poprawy, tu byłaby akcja reprezentująca brak auta

def znajdz_zabe(obs, zaba):  #optymalizacja: w pixel_x i pixel_y mamy przednia lewa lapke!!!
    #idziemy od dołu?
    pixel_x = 0;
    pixel_y = 0;

    for linijka in obs:
        pixel_x = 0;
        for pixel in linijka:
            if((pixel==[110, 156, 66]).all()):
                zaba.pozycjay = pixel_y;
                return [pixel_x, pixel_y];
            pixel_x+=1;
        pixel_y+=1;

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
    zabcia = zaba_agent.zaba_agent()
    while(not terminated and not truncated): #na potrzeby testu, jedna zaba do smierci lub znudzenia;)
        i+=1
        if i % 6 <= 3:
            zaba_x, zaba_y = znajdz_zabe(obs, zabcia);
            action = zabcia.pobierz_akcje(env, szukajaut(obs, zaba_x, zaba_y));
        else:
            #konieczne, poniewaz symulujemy przyciski - jesli akcja sie powtorzy zostanie wykonanana tylko raz 
            #mogloby to zaburzyc proces uczenia sie imo
            action = 0
        obs, reward, terminated, truncated, info = env.step(action)
 

    env.close()

if __name__ == '__main__':
    run()