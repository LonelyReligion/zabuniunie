import gymnasium as gym
import numpy #moze do generowania seeda?
import zaba_agent

def znajdz_zabe(obs):  #optymalizacja: w pixel_x i pixel_y mamy przednia lewa lapke!!!
    #idziemy od dołu?
    pixel_x = 0;
    pixel_y = 0;
    zaba_znaleziona = False;

    for linijka in obs:
        pixel_x = 0;
        for pixel in linijka:
            if((pixel==[110, 156, 66]).all()):
                print("Mamy fragment żaby! Yippee" + " " + str(pixel_x));
                zaba_znaleziona = True;
                return [pixel_x, pixel_y]
            pixel_x+=1;
        pixel_y+=1;
    
#def popatrz()

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
        znajdz_zabe(obs);
        if i % 6 <= 3:
            action = zabcia.pobierz_akcje(env, obs)
        else:
            #konieczne, poniewaz symulujemy przyciski - jesli akcja sie powtorzy zostanie wykonanana tylko raz 
            #mogloby to zaburzyc proces uczenia sie imo
            action = 0
        obs, reward, terminated, truncated, info = env.step(action)
 

    env.close()

if __name__ == '__main__':
    run()